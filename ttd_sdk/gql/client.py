from dataclasses import dataclass, make_dataclass
from enum import Enum
from pathlib import Path
from typing import Optional, TypeVar, Generic, Any
import httpx

T = TypeVar('T')

class Environment(Enum):
    SANDBOX = "https://ext-api.sb.thetradedesk.com/graphql"
    PRODUCTION = "https://api.gen.adsrvr.org/graphql"

@dataclass
class GraphQLResponse(Generic[T]):
    data: Optional[T]
    errors: list[dict]

class TTDGraphQLClient:
    def __init__(self, api_key: str, environment: Environment = Environment.SANDBOX):
        self.client = httpx.AsyncClient(
            headers={
                "TTD-Auth": api_key,
                "Content-Type": "application/json"
            }
        )
        self.url = environment.value
        self._query_cache = {}
        self._type_cache = {}

    def load_query(self, name: str) -> str:
        if name not in self._query_cache:
            query_path = Path(__file__).parent / 'queries' / f"{name}.graphql"
            print(f"Looking for query at: {query_path}")  # Debug path
            if not query_path.exists():
                raise FileNotFoundError(f"Query file not found: {query_path}")
            self._query_cache[name] = query_path.read_text()
        return self._query_cache[name]

    def create_type_from_data(self, name: str, data: dict) -> type:
        if name in self._type_cache:
            return self._type_cache[name]

        fields = []
        for key, value in data.items():
            if isinstance(value, dict):
                field_type = self.create_type_from_data(f"{name}_{key}", value)
            elif isinstance(value, list) and value and isinstance(value[0], dict):
                item_type = self.create_type_from_data(f"{name}_{key}_item", value[0])
                field_type = list[item_type]
            else:
                field_type = type(value) if value is not None else Any

            fields.append((key, field_type))

        cls = make_dataclass(name, fields)
        self._type_cache[name] = cls
        return cls

    async def execute_query(
        self, 
        query_name: str,
        variables: Optional[dict] = None
    ) -> GraphQLResponse[Any]:
        query = self.load_query(query_name)
        
        # Debug info
        print(f"Sending request to: {self.url}")
        print(f"Headers: {self.client.headers}")
        print(f"Query: {query[:200]}...")  # First 200 chars of query
        
        response = await self.client.post(
            self.url,
            json={"query": query, "variables": variables}
        )
        
        # Debug info
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text[:500]}...")  # First 500 chars of response
        
        if not response.is_success:
            return GraphQLResponse(None, [{"message": f"HTTP {response.status_code}"}])
            
        result = response.json()
        
        if result.get("data"):
            # Get the first key in data (usually the operation name)
            operation_name = next(iter(result["data"]))
            operation_data = result["data"][operation_name]
            
            # Create a type based on the response structure
            response_type = self.create_type_from_data(
                query_name.title(), 
                operation_data if isinstance(operation_data, dict) else {"result": operation_data}
            )
            
            # Convert the data to our generated type
            typed_data = response_type(**operation_data)
            return GraphQLResponse(typed_data, result.get("errors", []))
        
        return GraphQLResponse(None, result.get("errors", []))
    
    async def close(self):
        await self.client.aclose()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *args):
        await self.close()
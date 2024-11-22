import httpx
import json
from enum import Enum
from pathlib import Path
from typing import Optional

from ..logging import (
    configure_sdk_logging, 
    get_logger, 
    LogLevel,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL
)

logger = get_logger(__name__)

class TTDGraphQLClient:
    def __init__(
        self, 
        api_key: str, 
        sandbox: bool = True,
        timeout: float = 120.0,
        max_retries: int = 3,
        log_level: Optional[LogLevel | int] = None,
        log_file: Optional[str] = None
    ):
        if log_level or log_file:
            configure_sdk_logging(
                level=log_level,
                log_file=log_file
            )
        
        logger.info("Initializing GraphQL client")
        logger.debug(f"Sandbox mode: {sandbox}")
        
        self.base_url = (
            "https://ext-api.sb.thetradedesk.com/graphql" if sandbox
            else "https://api.gen.adsrvr.org/graphql"
        )
        
        self.client = httpx.AsyncClient(
            headers={
                "TTD-Auth": api_key,
                "Content-Type": "application/json"
            },
            timeout=timeout
        )
        self._query_cache = {}
        
    def load_query(self, name: str) -> str:
        if name not in self._query_cache:
            query_path = Path(__file__).parent / 'queries' / f"{name}.graphql"
            logger.debug(f"Loading query from path: {query_path}")
            
            if not query_path.exists():
                logger.error(f"Query file not found: {query_path}")
                raise FileNotFoundError(f"Query file not found: {query_path}")
                
            self._query_cache[name] = query_path.read_text()
            logger.debug(f"Cached query: {name}")
            
        return self._query_cache[name]

    async def execute_query(self, query_name: str, variables: dict = None, max_retries: int = 3) -> dict:
        logger.info(f"Executing query: {query_name}")
        logger.debug(f"Query variables: {variables}")
        
        query = self.load_query(query_name)
        retries = 0
        
        while retries <= max_retries:
            try:
                response = await self.client.post(
                    self.base_url,
                    json={"query": query, "variables": variables or {}}
                )
                
                # Handle API Gateway rate limits (HTTP 429)
                if response.status_code == 429 and retries < max_retries:
                    retries += 1
                    logger.warning(f"API Gateway rate limit hit, attempt {retries} of {max_retries}. Waiting 61 seconds...")
                    await httpx.AsyncClient.sleep(61)
                    continue
                    
                # Handle other non-200 responses
                if not response.is_success:
                    logger.error(f"Query failed with status {response.status_code}")
                    logger.error(f"Response body: {response.text}")
                    return {"errors": [{"message": f"HTTP {response.status_code}", "details": response.text}]}
                    
                response_json = response.json()
                
                # Handle GraphQL system errors
                if "errors" in response_json:
                    error = response_json["errors"][0]
                    if error.get("extensions", {}).get("code") == "RESOURCE_LIMIT_EXCEEDED" and retries < max_retries:
                        retries += 1
                        logger.warning(f"GraphQL rate/complexity limit hit, attempt {retries} of {max_retries}. Waiting 61 seconds...")
                        await httpx.AsyncClient.sleep(61)
                        continue
                    logger.error(f"GraphQL errors: {json.dumps(response_json['errors'], indent=2)}")
                
                return response_json
                
            except httpx.TimeoutException as e:
                logger.error(f"Request timed out: {str(e)}")
                return {"errors": [{"message": "Request timed out", "details": str(e)}]}
            except Exception as e:
                logger.error(f"Unexpected error during query execution: {str(e)}")
                return {"errors": [{"message": "Unexpected error", "details": str(e)}]}
    
    async def close(self):
        logger.info("Closing client connection")
        await self.client.aclose()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *args):
        await self.close()

    async def fetch_all(self, query_name: str, variables: dict = None) -> dict:
        logger.info(f"Fetching all pages for query: {query_name}")
        variables = variables or {}
        all_data = {}
        
        def find_cursors(data: dict) -> dict:
            """Find all fields that have next pages and their cursors."""
            cursors = {}
            
            def traverse(obj: dict):
                if not isinstance(obj, dict):
                    return
                    
                for key, value in obj.items():
                    if isinstance(value, dict):
                        # Check if this field has pagination
                        if "nodes" in value and "pageInfo" in value:
                            if value["pageInfo"].get("hasNextPage"):
                                cursors[f"{key}_cursor"] = value["pageInfo"]["endCursor"]
                                logger.debug(f"Found cursor for field {key}: {value['pageInfo']['endCursor']}")
                        traverse(value)
            
            traverse(data)
            return cursors

        def merge_data(existing: dict, new_data: dict) -> dict:
            """Merge paginated data, combining node arrays."""
            if not existing:
                return new_data
            
            def merge_dict(current: dict, new: dict):
                for key, value in new.items():
                    if key not in current:
                        current[key] = value
                    elif isinstance(value, dict):
                        if "nodes" in value:
                            current[key]["nodes"].extend(value["nodes"])
                            current[key]["pageInfo"] = value["pageInfo"]
                        else:
                            merge_dict(current[key], value)
            
            result = dict(existing)
            merge_dict(result, new_data)
            return result

        while True:
            response = await self.execute_query(query_name, variables)
            
            if "errors" in response:
                return response
            
            data = response.get("data", {})
            logger.debug(f"Response data: {data}")
            
            all_data = merge_data(all_data, data)
            
            # Find any fields that have next pages
            next_cursors = find_cursors(data)
            logger.debug(f"Found cursors: {next_cursors}")
            
            if not next_cursors:
                break
            
            # Update variables with new cursors
            variables.update(next_cursors)
            logger.debug(f"Next page variables: {variables}")
        
        return {"data": all_data}
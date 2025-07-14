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
        
        self.client = httpx.Client(
            headers={
                "TTD-Auth": api_key,
                "Content-Type": "application/json"
            },
            timeout=timeout
        )
        self._query_cache = {}
        
    def load_query(self, name: str) -> str:
        if name not in self._query_cache:
            queries_dir = Path(__file__).parent / 'queries'
            query_path = None
            
            for path in queries_dir.rglob("*.graphql"):
                if path.stem == name:
                    query_path = path
                    break
                    
            if not query_path:
                logger.error(f"Query file not found: {name}.graphql")
                raise FileNotFoundError(f"Query file not found: {name}.graphql")
                
            self._query_cache[name] = query_path.read_text()
            logger.debug(f"Cached query from {query_path}")
            
        return self._query_cache[name]

    def execute_user_query(self, query: str, variables: dict = None, max_retries: int = 3) -> dict:
        """Execute a user-provided GraphQL query string."""
        logger.info(f"Executing user query: {query[:50]}{'...' if len(query) > 50 else ''}")
        logger.debug(f"Query variables: {variables}")
        
        retries = 0
        
        while retries <= max_retries:
            response = self.client.post(
                self.base_url,
                json={"query": query, "variables": variables or {}}
            )
            
            if response.status_code == 429 and retries < max_retries:
                retries += 1
                logger.warning(f"API Gateway rate limit hit, attempt {retries} of {max_retries}. Waiting 61 seconds...")
                import time
                time.sleep(61)
                continue
                
            response_json = response.json()
            if "errors" in response_json:
                logger.error(f"GraphQL errors: {json.dumps(response_json['errors'], indent=2)}")
                raise Exception("GraphQL query failed - see logs for details")
            
            return response_json

    def execute_query(self, query_name: str, variables: dict = None, max_retries: int = 3) -> dict:
        logger.info(f"Executing query: {query_name}")
        logger.debug(f"Query variables: {variables}")
        
        query = self.load_query(query_name)
        retries = 0
        
        while retries <= max_retries:
            response = self.client.post(
                self.base_url,
                json={"query": query, "variables": variables or {}}
            )
            
            if response.status_code == 429 and retries < max_retries:
                retries += 1
                logger.warning(f"API Gateway rate limit hit, attempt {retries} of {max_retries}. Waiting 61 seconds...")
                import time
                time.sleep(61)
                continue
                
            response_json = response.json()
            if "errors" in response_json:
                logger.error(f"GraphQL errors: {json.dumps(response_json['errors'], indent=2)}")
                raise Exception("GraphQL query failed - see logs for details")
            
            return response_json
    
    def close(self):
        logger.info("Closing client connection")
        self.client.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def fetch_all(self, query_name: str, variables: dict = None) -> dict:
        logger.info(f"Fetching all pages for query: {query_name}")
        variables = variables or {}
        all_data = {}
        
        def find_cursors(data: dict) -> dict:
            """Find all fields that have next pages and their cursors."""
            cursors = {}
            
            def traverse(obj: dict, path: list[str] = None):
                path = path or []
                if not isinstance(obj, dict):
                    return
                    
                for key, value in obj.items():
                    current_path = path + [key]
                    if isinstance(value, dict):
                        # Check if this field has pagination
                        if "nodes" in value and "pageInfo" in value:
                            if value["pageInfo"].get("hasNextPage"):
                                cursor_name = "_".join(current_path) + "_cursor"
                                cursors[cursor_name] = value["pageInfo"]["endCursor"]
                                logger.debug(f"Found cursor at {'.'.join(current_path)}: {value['pageInfo']['endCursor']}")
                        traverse(value, current_path)
            
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
            response = self.execute_query(query_name, variables)
            
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
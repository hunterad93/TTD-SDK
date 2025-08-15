from typing import Iterator, Optional, Dict, Any, List
from ..models.base import ApiObject

class RedsFeedResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "redsfeed"
    
    def query(
        self,
        page_size: Optional[int] = 100,
        page_start_index: int = 0,
        partner_id: Optional[str] = None,
        search_terms: Optional[List[str]] = None,
        sort_fields: Optional[List[Dict[str, Any]]] = None,
    ) -> Iterator[ApiObject]:
        """
        Get metadata of all available feeds.
        
        Args:
            page_size: Number of results per page (100-1000 recommended)
            page_start_index: Zero-based index to start the page
            partner_id: ID of the partner (uses primary if not specified)
            search_terms: List of search terms to filter feeds
            sort_fields: List of sort field configurations
        """
        data = {
            "PageSize": page_size,
            "PageStartIndex": page_start_index
        }
        
        if partner_id:
            data["PartnerId"] = partner_id
        if search_terms:
            data["SearchTerms"] = search_terms
        if sort_fields:
            data["SortFields"] = sort_fields
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query",
            data=data,
            page_size=page_size or 100
        ):
            yield ApiObject(**result)
    
    def query_all(
        self,
        partner_id: Optional[str] = None,
        search_terms: Optional[List[str]] = None,
        sort_fields: Optional[List[Dict[str, Any]]] = None,
    ) -> List[ApiObject]:
        """
        Get all available feeds without pagination.
        
        Args:
            partner_id: ID of the partner (uses primary if not specified)
            search_terms: List of search terms to filter feeds
            sort_fields: List of sort field configurations
        """
        data = {
            "PageSize": None,
            "PageStartIndex": 0
        }
        
        if partner_id:
            data["PartnerId"] = partner_id
        if search_terms:
            data["SearchTerms"] = search_terms
        if sort_fields:
            data["SortFields"] = sort_fields
        
        response = self.client.post(f"{self.base_path}/query", data)
        return [ApiObject(**feed) for feed in response.get("Result", [])]

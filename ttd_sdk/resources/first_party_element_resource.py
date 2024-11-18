from typing import Iterator, Optional, Dict, List
from ..models.base import ApiObject

class FirstPartyElementResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "dmp/firstparty"
    
    def get(self, element_id: int, advertiser_id: str) -> ApiObject:
        """
        Get details of a specific first party data element.
        """
        elements = list(self.list(
            advertiser_id=advertiser_id,
            first_party_data_ids=[element_id],
            page_size=1000
        ))
        if not elements:
            raise ValueError(f"No element found with ID {element_id}")
        return elements[0]
    
    def list(
        self,
        advertiser_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        first_party_data_ids: Optional[List[int]] = None,
        search_terms: Optional[List[str]] = None,
    ) -> Iterator[ApiObject]:
        """
        Get a paginated list of first party data elements with optional filtering.
        
        Args:
            advertiser_id: The platform ID of the advertiser
            page_size: Number of results per page (100-1000 recommended)
            sort_fields: Optional list of sort field configurations
            first_party_data_ids: Optional list of specific first party data IDs
            search_terms: Optional list of search terms to filter by
        """
            
        data = {"AdvertiserId": advertiser_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        if first_party_data_ids:
            data["FirstPartyDataIds"] = first_party_data_ids
        if search_terms:
            data["SearchTerms"] = search_terms
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/advertiser",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)
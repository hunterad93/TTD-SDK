from typing import Iterator, Optional, Dict, List
from ..models.base import ApiObject

class AdvertiserResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "advertiser"
    
    def get(self, advertiser_id: str) -> ApiObject:
        """
        Get an advertiser by ID.
        """
        response = self.client.get(f"{self.base_path}/{advertiser_id}")
        return ApiObject(**response)
    
    def update(self, advertiser_id: str, advertiser: ApiObject) -> ApiObject:
        """
        Update an existing advertiser.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = advertiser.to_dict()
        response = self.client.put(f"{self.base_path}/{advertiser_id}", data)
        return ApiObject(**response)
    
    def list(
        self,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        search_terms: Optional[List[str]] = None,
        availabilities: Optional[List[str]] = None,
    ) -> Iterator[ApiObject]:
        """
        Get a paginated list of all advertisers for the partner.
        
        Args:
            page_size: Number of results per page (100-1000 recommended)
            sort_fields: Optional list of sort field configurations
            search_terms: Optional list of search terms to filter by
            availabilities: Optional list of availability states to filter by
        """
            
        data = {"PartnerId": self.client.partner_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        if search_terms:
            data["SearchTerms"] = search_terms
        if availabilities:
            data["Availabilities"] = availabilities
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/partner",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)
    
    def get_name(self, advertiser_id: str) -> str:
        """
        Get an advertiser's name by ID.
        """
        response = self.client.get(f"{self.base_path}/name/{advertiser_id}")
        return response["Name"]
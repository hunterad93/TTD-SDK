from typing import Iterator, Optional, Dict, List
from ..models.base import ApiObject

class CreativeResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "creative"
    
    def create(self, creative: ApiObject) -> ApiObject:
        """
        Create a new creative.
        """
        if not getattr(creative, 'CreativeName', None) or not getattr(creative, 'AdvertiserId', None):
            raise ValueError("CreativeName and AdvertiserId are required")
        
        data = creative.to_dict()
        response = self.client.post(self.base_path, data)
        return ApiObject(**response)
    
    def get(self, creative_id: str) -> ApiObject:
        """
        Get a creative by ID.
        """
        response = self.client.get(f"{self.base_path}/{creative_id}")
        return ApiObject(**response)
    
    def update(self, creative_id: str, creative: ApiObject) -> ApiObject:
        """
        Update an existing creative.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = creative.to_dict()
        response = self.client.put(f"{self.base_path}/{creative_id}", data)
        return ApiObject(**response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        search_terms: Optional[List[str]] = None,
        availabilities: Optional[List[str]] = None,
    ) -> Iterator[ApiObject]:
        """
        Get a paginated list of creatives for an advertiser.
        
        Args:
            advertiser_id: The platform ID of the advertiser
            page_size: Number of results per page (100-1000 recommended)
            sort_fields: Optional list of sort field configurations
            search_terms: Optional list of search terms to filter by
            availabilities: Optional list of availability states to filter by
        """
        data = {"AdvertiserId": advertiser_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        if search_terms:
            data["SearchTerms"] = search_terms
        if availabilities:
            data["Availabilities"] = availabilities
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/advertiser",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)
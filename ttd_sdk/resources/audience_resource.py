from typing import Iterator, Optional, Dict, List
from ..models.audience import Audience

class AudienceResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "audience"
    
    def create(self, audience: Audience) -> Audience:
        """
        Create a new audience.
        """
        if not audience.audience_name or not audience.advertiser_id:
            raise ValueError("audience_name and advertiser_id are required")
        
        data = audience.model_dump(exclude_none=True)
        response = self.client.post(self.base_path, data)
        return Audience.model_validate(response)
    
    def get(self, audience_id: str) -> Audience:
        """
        Get an audience by ID.
        """
        response = self.client.get(f"{self.base_path}/{audience_id}")
        return Audience.model_validate(response)
    
    def update(self, audience_id: str, audience: Audience) -> Audience:
        """
        Update an existing audience.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = audience.model_dump(exclude_none=True)
        response = self.client.put(f"{self.base_path}/{audience_id}", data)
        return Audience.model_validate(response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        search_terms: Optional[List[str]] = None,
    ) -> Iterator[Audience]:
        """
        Get a paginated list of audiences for an advertiser.
        
        Args:
            advertiser_id: The platform ID of the advertiser
            page_size: Number of results per page (100-1000 recommended)
            sort_fields: Optional list of sort field configurations
            search_terms: Optional list of search terms to filter by
        """
            
        data = {"AdvertiserId": advertiser_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        if search_terms:
            data["SearchTerms"] = search_terms
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/advertiser",
            data=data,
            page_size=page_size
        ):
            yield Audience.model_validate(result) 
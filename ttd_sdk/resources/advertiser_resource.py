from typing import Iterator, Optional, Dict, List
from ..models.advertiser import Advertiser

class AdvertiserResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "advertiser"
    
    def get(self, advertiser_id: str) -> Advertiser:
        """
        Get an advertiser by ID.
        """
        response = self.client.get(f"{self.base_path}/{advertiser_id}")
        return Advertiser.model_validate(response)
    
    def update(self, advertiser_id: str, advertiser: Advertiser) -> Advertiser:
        """
        Update an existing advertiser.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = advertiser.model_dump(exclude_none=True)
        response = self.client.put(f"{self.base_path}/{advertiser_id}", data)
        return Advertiser.model_validate(response)
    
    def list(
        self,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        search_terms: Optional[List[str]] = None,
        availabilities: Optional[List[str]] = None,
    ) -> Iterator[Advertiser]:
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
            yield Advertiser.model_validate(result)
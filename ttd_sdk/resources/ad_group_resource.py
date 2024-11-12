from typing import Iterator, Optional, Dict, List
from ..models.ad_group import AdGroup

class AdGroupResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "adgroup"
    
    def get(self, ad_group_id: str) -> AdGroup:
        """
        Get an ad group by ID.
        """
        response = self.client.get(f"{self.base_path}/{ad_group_id}")
        return AdGroup.model_validate(response)
    
    def create(self, ad_group: AdGroup) -> AdGroup:
        """
        Create a new ad group.
        """
        if not ad_group.ad_group_name or not ad_group.campaign_id:
            raise ValueError("ad_group_name and campaign_id are required")
        
        data = ad_group.model_dump(exclude_none=True)
        response = self.client.post(self.base_path, data)
        return AdGroup.model_validate(response)
    
    def update(self, ad_group_id: str, ad_group: AdGroup) -> AdGroup:
        """
        Update an existing ad group.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = ad_group.model_dump(exclude_none=True)
        response = self.client.put(f"{self.base_path}/{ad_group_id}", data)
        return AdGroup.model_validate(response)
    
    def list_by_campaign(
        self,
        campaign_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        search_terms: Optional[List[str]] = None,
        availabilities: Optional[List[str]] = None,
    ) -> Iterator[AdGroup]:
        """
        Get a paginated list of ad groups for a campaign.
        
        Args:
            campaign_id: The ID of the campaign
            page_size: Number of results per page (100-1000 recommended)
            sort_fields: Optional list of sort field configurations
            search_terms: Optional list of search terms to filter by
            availabilities: Optional list of availability states to filter by
        """
        data = {"CampaignId": campaign_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        if search_terms:
            data["SearchTerms"] = search_terms
        if availabilities:
            data["Availabilities"] = availabilities
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/campaign",
            data=data,
            page_size=page_size
        ):
            yield AdGroup.model_validate(result) 
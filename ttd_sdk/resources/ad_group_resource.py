from typing import Iterator, Optional, Dict, List
from ..models.base import ApiObject

class AdGroupResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "adgroup"
    
    def get(self, ad_group_id: str) -> ApiObject:
        """Get an ad group by ID."""
        response = self.client.get(f"{self.base_path}/{ad_group_id}")
        return ApiObject(**response)
    
    def create(self, ad_group: ApiObject) -> ApiObject:
        """Create a new ad group."""
        if not getattr(ad_group, 'AdGroupName', None) or not getattr(ad_group, 'CampaignId', None):
            raise ValueError("AdGroupName and CampaignId are required")
        
        data = ad_group.to_dict()
        response = self.client.post(self.base_path, data)
        return ApiObject(**response)
    
    def update(self, ad_group_id: str, ad_group: ApiObject) -> ApiObject:
        """
        Update an existing ad group.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = ad_group.to_dict()
        data["AdGroupId"] = ad_group_id
        
        response = self.client.put(self.base_path, data)
        return ApiObject(**response)
    
    def list_by_campaign(
        self,
        campaign_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        search_terms: Optional[List[str]] = None,
        availabilities: Optional[List[str]] = None,
    ) -> Iterator[ApiObject]:
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
            yield ApiObject(**result) 

    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
        search_terms: Optional[List[str]] = None,
        availabilities: Optional[List[str]] = None,
        is_template_ad_groups: Optional[bool] = None,
    ) -> Iterator[ApiObject]:
        """Get a paginated list of ad groups for an advertiser."""
        data = {"AdvertiserId": advertiser_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        if search_terms:
            data["SearchTerms"] = search_terms
        if availabilities:
            data["Availabilities"] = availabilities
        if is_template_ad_groups is not None:
            data["IsTemplateAdGroups"] = is_template_ad_groups
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/advertiser",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)

        
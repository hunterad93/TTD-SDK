from typing import Iterator, Optional, Dict, Any, List
from ..models.campaign import Campaign

class CampaignResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "campaign"
    
    def create(self, campaign: Campaign) -> Campaign:
        """
        Create a new campaign.
        """
        # Validate that either flights or start_date + budget is provided, but not both
        has_flights = bool(campaign.campaign_flights)
        has_start_budget = bool(campaign.start_date and campaign.budget)
        
        if has_flights == has_start_budget:
            raise ValueError(
                "Must specify either campaign_flights or (start_date and budget), but not both"
            )
        
        # Ensure required fields are present
        if not campaign.campaign_name or not campaign.advertiser_id:
            raise ValueError("campaign_name and advertiser_id are required")
            
        if not campaign.primary_channel or not campaign.primary_goal:
            raise ValueError("primary_channel and primary_goal are required")
            
        if campaign.campaign_conversion_reporting_columns is None:
            campaign.campaign_conversion_reporting_columns = []
            
        # Handle ballot measure campaigns
        if campaign.is_ballot_measure and not campaign.ballot_measure_profile:
            raise ValueError("ballot_measure_profile is required when is_ballot_measure is True")
            
        # Handle pacing mode validation
        if campaign.pacing_mode == "Off" and not (campaign.daily_budget or campaign.daily_budget_in_impressions):
            raise ValueError(
                "When pacing_mode is Off, either daily_budget or daily_budget_in_impressions is required"
            )
            
        campaign_data = campaign.model_dump(
            exclude_none=True
        )
        
        response = self.client.post(self.base_path, campaign_data)
        return Campaign.model_validate(response)
    
    def get(self, campaign_id: str) -> Campaign:
        response = self.client.get(f"{self.base_path}/{campaign_id}")
        return Campaign.model_validate(response)
    
    def update(self, campaign_id: str, campaign: Campaign) -> Campaign:
        """
        Update an existing campaign.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        campaign_data = campaign.model_dump(exclude_none=True)
        
        response = self.client.put(f"{self.base_path}/{campaign_id}", campaign_data)
        return Campaign.model_validate(response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 100,
        availabilities: Optional[List[str]] = None,
        search_terms: Optional[List[str]] = None,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[Campaign]:
        """
        Get a paginated list of campaigns for an advertiser.
        
        Args:
            advertiser_id: The platform ID of the advertiser
            page_size: Number of results per page (100-1000 recommended)
            availabilities: Optional list of availability states to filter by
            search_terms: Optional list of search terms to filter by
            sort_fields: Optional list of sort field configurations
        """
        data = {"AdvertiserId": advertiser_id}
        
        if availabilities:
            data["Availabilities"] = availabilities
        if search_terms:
            data["SearchTerms"] = search_terms
        if sort_fields:
            data["SortFields"] = sort_fields
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/advertiser",
            data=data,
            page_size=page_size
        ):
            yield Campaign.model_validate(result)
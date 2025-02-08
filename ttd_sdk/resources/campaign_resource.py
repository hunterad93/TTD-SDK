from typing import Iterator, Optional, Dict, Any, List
from ..models.base import ApiObject

class CampaignResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "campaign"
    
    def create(self, campaign: ApiObject) -> ApiObject:
        """
        Create a new campaign.
        """
        # Validate that either flights or start_date + budget is provided, but not both
        has_flights = bool(getattr(campaign, 'CampaignFlights', None))
        has_start_budget = bool(getattr(campaign, 'StartDate', None) and getattr(campaign, 'Budget', None))
        
        if has_flights == has_start_budget:
            raise ValueError(
                "Must specify either CampaignFlights or (StartDate and Budget), but not both"
            )
        
        # Ensure required fields are present
        if not getattr(campaign, 'CampaignName', None) or not getattr(campaign, 'AdvertiserId', None):
            raise ValueError("CampaignName and AdvertiserId are required")
            
        if not getattr(campaign, 'PrimaryChannel', None) or not getattr(campaign, 'PrimaryGoal', None):
            raise ValueError("PrimaryChannel and PrimaryGoal are required")
            
        if getattr(campaign, 'CampaignConversionReportingColumns', None) is None:
            setattr(campaign, 'CampaignConversionReportingColumns', [])
            
        # Handle ballot measure campaigns
        if getattr(campaign, 'IsBallotMeasure', False) and not getattr(campaign, 'BallotMeasureProfile', None):
            raise ValueError("BallotMeasureProfile is required when IsBallotMeasure is True")
            
        # Handle pacing mode validation
        if (getattr(campaign, 'PacingMode', None) == "Off" and 
            not (getattr(campaign, 'DailyBudget', None) or getattr(campaign, 'DailyBudgetInImpressions', None))):
            raise ValueError(
                "When PacingMode is Off, either DailyBudget or DailyBudgetInImpressions is required"
            )
            
        data = campaign.to_dict()
        response = self.client.post(self.base_path, data)
        return ApiObject(**response)
    
    def get(self, campaign_id: str) -> ApiObject:
        """Get a campaign by ID."""
        response = self.client.get(f"{self.base_path}/{campaign_id}")
        return ApiObject(**response)
    
    def update(self, campaign_id: str, campaign: ApiObject) -> ApiObject:
        """
        Update an existing campaign.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = campaign.to_dict()
        data["CampaignId"] = campaign_id
        
        response = self.client.put(self.base_path, data)
        return ApiObject(**response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 100,
        availabilities: Optional[List[str]] = None,
        search_terms: Optional[List[str]] = None,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[ApiObject]:
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
            yield ApiObject(**result)
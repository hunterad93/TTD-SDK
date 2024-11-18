from datetime import datetime
from typing import Iterator, Optional, List
from ..models.base import ApiObject

class ActivityLogResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "activity"
    
    def get(self, activity_log_id: int) -> ApiObject:
        """Get an activity log entry by ID."""
        response = self.client.get(f"{self.base_path}/{activity_log_id}")
        return ApiObject(**response)
    
    def list_by_campaign(
        self,
        campaign_id: str,
        page_size: int = 100,
        date_start: Optional[datetime] = None,
        date_end: Optional[datetime] = None,
        include_bid_line_details: bool = False,
        source: Optional[str] = None,
        updated_by: Optional[str] = None,
        updated_in: Optional[List[str]] = None,
    ) -> Iterator[ApiObject]:
        """Get activity logs for a campaign."""
        data = {
            "CampaignId": campaign_id,
            "IncludeBidLineDetails": include_bid_line_details,
        }
        
        if date_start:
            data["DateTimeStartUtc"] = date_start.isoformat()
        if date_end:
            data["DateTimeEndUtc"] = date_end.isoformat()
        if source:
            data["Source"] = source
        if updated_by:
            data["UpdatedBy"] = updated_by
        if updated_in:
            data["UpdatedIn"] = updated_in
            
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/campaign",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)
    
    def list_by_ad_group(
        self,
        ad_group_id: str,
        page_size: int = 100,
        date_start: Optional[datetime] = None,
        date_end: Optional[datetime] = None,
        include_bid_line_details: bool = False,
        source: Optional[str] = None,
        updated_by: Optional[str] = None,
        updated_in: Optional[List[str]] = None,
    ) -> Iterator[ApiObject]:
        """Get activity logs for an ad group."""
        data = {
            "AdGroupId": ad_group_id,
            "IncludeBidLineDetails": include_bid_line_details,
        }
        
        if date_start:
            data["DateTimeStartUtc"] = date_start.isoformat()
        if date_end:
            data["DateTimeEndUtc"] = date_end.isoformat()
        if source:
            data["Source"] = source
        if updated_by:
            data["UpdatedBy"] = updated_by
        if updated_in:
            data["UpdatedIn"] = updated_in
            
        for result in self.client.post_with_pagination(
            f"{self.base_path}/query/adgroup",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)
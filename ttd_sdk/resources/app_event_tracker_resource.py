from typing import Iterator, Optional, Dict, Any, List
from ..models.app_event_tracker import AppEventTracker

class AppEventTrackerResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "tracking/appeventtracker"
    
    def create(self, tracker: AppEventTracker) -> AppEventTracker:
        """
        Create a new app event tracker.
        """
        if not tracker.app_event_tracker_name or not tracker.advertiser_id:
            raise ValueError("app_event_tracker_name and advertiser_id are required")
            
        if not tracker.tracked_app_operating_system or not tracker.tracked_app_vendor_id:
            raise ValueError("tracked_app_operating_system and tracked_app_vendor_id are required")
        
        data = tracker.model_dump(exclude_none=True)
        response = self.client.post(self.base_path, data)
        return AppEventTracker.model_validate(response)
    
    def get(self, tracker_id: str) -> AppEventTracker:
        """
        Get an app event tracker by ID.
        """
        response = self.client.get(f"{self.base_path}/{tracker_id}")
        return AppEventTracker.model_validate(response)
    
    def update(self, tracker_id: str, tracker: AppEventTracker) -> AppEventTracker:
        """
        Update an existing app event tracker.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = tracker.model_dump(exclude_none=True)
        response = self.client.put(f"{self.base_path}/{tracker_id}", data)
        return AppEventTracker.model_validate(response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[AppEventTracker]:
        """
        Get a paginated list of app event trackers for an advertiser.
        
        Args:
            advertiser_id: The platform ID of the advertiser
            page_size: Number of results per page (100-1000 recommended)
            sort_fields: Optional list of sort field configurations
        """
            
        data = {"AdvertiserId": advertiser_id}
        
        if sort_fields:
            data["SortFields"] = sort_fields
        
        for result in self.client.post_with_pagination(
            f"{self.base_path}withactivity/advertiser/query",
            data=data,
            page_size=page_size
        ):
            yield AppEventTracker.model_validate(result) 
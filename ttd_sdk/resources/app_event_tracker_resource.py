from typing import Iterator, Optional, Dict, Any, List
from ..models.base import ApiObject

class AppEventTrackerResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "tracking/appeventtracker"
    
    def create(self, tracker: ApiObject) -> ApiObject:
        """
        Create a new app event tracker.
        """
        if not getattr(tracker, 'AppEventTrackerName', None) or not getattr(tracker, 'AdvertiserId', None):
            raise ValueError("AppEventTrackerName and AdvertiserId are required")
            
        if not getattr(tracker, 'TrackedAppOperatingSystem', None) or not getattr(tracker, 'TrackedAppVendorId', None):
            raise ValueError("TrackedAppOperatingSystem and TrackedAppVendorId are required")
        
        data = tracker.to_dict()
        response = self.client.post(self.base_path, data)
        return ApiObject(**response)
    
    def get(self, tracker_id: str) -> ApiObject:
        """
        Get an app event tracker by ID.
        """
        response = self.client.get(f"{self.base_path}/{tracker_id}")
        return ApiObject(**response)
    
    def update(self, tracker_id: str, tracker: ApiObject) -> ApiObject:
        """
        Update an existing app event tracker.
        
        Supports partial updates - only fields that are provided will be updated.
        """
        data = tracker.to_dict()
        response = self.client.put(f"{self.base_path}/{tracker_id}", data)
        return ApiObject(**response)
    
    def list_by_advertiser(
        self,
        advertiser_id: str,
        page_size: int = 1000,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[ApiObject]:
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
            yield ApiObject(**result) 
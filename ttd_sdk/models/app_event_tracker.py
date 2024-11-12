from typing import List, Optional, Dict
from pydantic import BaseModel

class TrackedEvent(BaseModel):
    DataEventTypeId: Optional[str] = None
    TrackedEventCode: Optional[str] = None
    TrackedEventName: Optional[str] = None
    TrackedEventType: Optional[str] = None
    TrackingTagId: Optional[str] = None

class AppEventTracker(BaseModel):
    AppEventTrackerId: Optional[str] = None
    AppEventTrackerName: Optional[str] = None
    AdvertiserId: Optional[str] = None
    Description: Optional[str] = None
    TrackedAppOperatingSystem: Optional[str] = None
    TrackedAppVendorId: Optional[int] = None
    TrackedEvents: Optional[List[TrackedEvent]] = None
    UseTrackedAppVendorAttribution: Optional[bool] = None
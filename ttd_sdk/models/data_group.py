from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class DataGroup(BaseModel):
    # Basic Information
    DataGroupId: Optional[str] = None
    DataGroupName: Optional[str] = None
    Description: Optional[str] = None
    AdvertiserId: Optional[str] = None
    
    # Data Elements
    FirstPartyDataIds: Optional[List[int]] = None
    ThirdPartyDataIds: Optional[List[str]] = None
    
    # Settings
    IsSharable: Optional[bool] = None
    SkipUnauthorizedThirdPartyData: Optional[bool] = None
    GeoForCounts: Optional[str] = None
    
    # Counts and Metrics (Read-only)
    UniqueUserCount: Optional[int] = None
    HouseholdCount: Optional[int] = None
    PersonsCount: Optional[int] = None
    ActiveIdsCountExpanded: Optional[bool] = None
    SuccessfullyRetrievedCounts: Optional[bool] = None
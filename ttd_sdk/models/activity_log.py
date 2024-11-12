from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class BidLineChange(BaseModel):
    Id: Optional[int] = None
    BidDimensionId: Optional[int] = None
    BidDimensionType: Optional[str] = None
    ChangeTimeUtc: Optional[datetime] = None
    Name: Optional[str] = None
    Op: Optional[str] = None
    ValueFrom: Optional[str] = None
    ValueTo: Optional[str] = None
    VolumeControlValueFrom: Optional[str] = None
    VolumeControlValueTo: Optional[str] = None

class ActivityLog(BaseModel):
    Id: Optional[int] = Field(None, description="Unique activity log ID")
    ActivityTimeUtc: Optional[datetime] = None
    ActivityRollupTimeUtc: Optional[datetime] = None
    Entity: Optional[str] = None
    Message: Optional[str] = None
    ModifiedByUser: Optional[str] = None
    Note: Optional[str] = Field(None, max_length=512)
    OwnerAdGroupId: Optional[str] = None
    OwnerCampaignId: Optional[str] = None
    Source: Optional[str] = None
    HasBidListChanges: Optional[bool] = None
    BidLineChanges: Optional[List[BidLineChange]] = None
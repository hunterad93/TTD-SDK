from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class LookAlikeModelDetails(BaseModel):
    FirstPartyDataId: Optional[int] = None
    LastGenerationDateUtc: Optional[datetime] = None
    LastRequestDateUtc: Optional[datetime] = None
    LookAlikeModelBuildStatus: Optional[str] = None
    LookAlikeModelResultStatus: Optional[str] = None

class FirstPartyElement(BaseModel):
    # Basic Information
    FirstPartyDataId: Optional[int] = None
    Name: Optional[str] = None
    DataType: Optional[str] = None
    
    # Counts and Metrics
    ActiveIdsCount: Optional[int] = None
    ActiveIdsWebCount: Optional[int] = None
    ActiveIdsInAppCount: Optional[int] = None
    ActiveIdsConnectedTvCount: Optional[int] = None
    ActiveHouseholdCount: Optional[int] = None
    ActivePersonsCount: Optional[int] = None
    ReceivedIdsCount: Optional[int] = None
    ActiveIdsCountExpanded: Optional[bool] = None
    
    # Look Alike Model Information
    LookAlikeModelEligibility: Optional[str] = None
    LookAlikeModelDetails: Optional[LookAlikeModelDetails] = None
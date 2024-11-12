from typing import Optional
from pydantic import BaseModel

from .base_types import CurrencyAmount

class ThirdPartyElement(BaseModel):
    # Basic Information
    ThirdPartyDataId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    BrandId: Optional[str] = None
    BrandName: Optional[str] = None
    FullPath: Optional[str] = None
    
    # Counts and Metrics
    ActiveIdsCount: Optional[int] = None
    ActiveIdsWebCount: Optional[int] = None
    ActiveIdsInAppCount: Optional[int] = None
    ActiveIdsConnectedTvCount: Optional[int] = None
    ActiveHouseholdCount: Optional[int] = None
    ActivePersonsCount: Optional[int] = None
    ReceivedIdsCount: Optional[int] = None
    ActiveIdsCountExpanded: Optional[bool] = None
    
    # Pricing
    CpmRate: Optional[CurrencyAmount] = None
    CpmRateInAdvertiserCurrency: Optional[CurrencyAmount] = None
    PercentOfMediaCostRate: Optional[float] = None
    
    # Features
    IsEligibleForSeeds: Optional[bool] = None

class ThirdPartyBrand(BaseModel):
    BrandId: Optional[str] = None
    BrandName: Optional[str] = None
    AllowedForPlanningTool: Optional[bool] = None
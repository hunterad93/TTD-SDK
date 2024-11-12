from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum
from pydantic import BaseModel

class CurrencyAmount(BaseModel):
    Amount: Optional[float] = None
    CurrencyCode: Optional[str] = None

class Fee(BaseModel):
    Amount: Optional[float] = None
    Description: Optional[str] = None
    FeeType: Optional[str] = None

class FeeCard(BaseModel):
    Fees: Optional[List[Fee]] = None
    OwnerId: Optional[str] = None
    OwnerType: Optional[str] = None
    StartDateUtc: Optional[datetime] = None

class BidList(BaseModel):
    BidListId: Optional[str] = None
    BidListAdjustmentType: Optional[str] = None
    BidListDimensions: Optional[List[str]] = None
    BidListSource: Optional[str] = None
    IsDefaultForDimension: Optional[bool] = None
    IsEnabled: Optional[bool] = None

class FrequencyConfig(BaseModel):
    CounterId: Optional[str] = None
    CounterName: Optional[str] = None
    FrequencyCap: Optional[int] = None
    FrequencyGoal: Optional[int] = None
    ResetIntervalInMinutes: Optional[int] = None

class Goal(BaseModel):
    CpaInAdvertiserCurrency: Optional[CurrencyAmount] = None
    CpcInAdvertiserCurrency: Optional[CurrencyAmount] = None
    CpcvInAdvertiserCurrency: Optional[CurrencyAmount] = None
    CtrInPercent: Optional[float] = None
    MaximizeLtvIncrementalReach: Optional[bool] = None
    MaximizeReach: Optional[bool] = None
    MiaozenOtpInPercent: Optional[float] = None
    NielsenOtpInPercent: Optional[float] = None
    ReturnOnAdSpendPercent: Optional[float] = None
    VcpmInAdvertiserCurrency: Optional[CurrencyAmount] = None
    VcrInPercent: Optional[float] = None
    ViewabilityInPercent: Optional[float] = None

class CategoryMapping(BaseModel):
    CategoryId: Optional[int] = None
    CategoryTaxonomyId: Optional[int] = None
    ExternalId: Optional[str] = None

class BaseCategory(BaseModel):
    CategoryId: Optional[int] = None
    CategoryName: Optional[str] = None
    CategoryTaxonomyId: Optional[int] = None
    CategoryTaxonomyName: Optional[str] = None
    CategoryTaxonomyVersion: Optional[str] = None
    Mappings: Optional[List[CategoryMapping]] = None

class CustomLabel(BaseModel):
    CustomLabelId: Optional[str] = None

class BaseTracking(BaseModel):
    AdvertiserId: Optional[str] = None
    Description: Optional[str] = None
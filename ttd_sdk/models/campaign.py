from datetime import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel

from .base_types import (
    CurrencyAmount, 
    Fee, 
    FeeCard, 
    BidList, 
    FrequencyConfig, 
    Goal,
    CustomLabel
)

class CampaignFlight(BaseModel):
    BudgetInAdvertiserCurrency: Optional[float] = None
    BudgetInImpressions: Optional[int] = None
    CampaignFlightId: Optional[int] = None
    CampaignId: Optional[str] = None
    DailyTargetInAdvertiserCurrency: Optional[float] = None
    DailyTargetInImpressions: Optional[int] = None
    EndDateExclusiveUtc: Optional[datetime] = None
    StartDateInclusiveUtc: Optional[datetime] = None

class Campaign(BaseModel):
    # Basic Information
    AdvertiserId: Optional[str] = None
    CampaignId: Optional[str] = None
    CampaignName: Optional[str] = None
    CampaignType: Optional[str] = None
    Availability: Optional[str] = None
    Version: Optional[str] = None
    
    # Budget related
    Budget: Optional[CurrencyAmount] = None
    DailyBudget: Optional[CurrencyAmount] = None
    BudgetInImpressions: Optional[int] = None
    DailyBudgetInImpressions: Optional[int] = None
    
    # Dates
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None
    CreatedAtUtc: Optional[datetime] = None
    
    # Goals
    PrimaryGoal: Optional[Goal] = None
    SecondaryGoal: Optional[Goal] = None
    TertiaryGoal: Optional[Goal] = None
    
    # Campaign settings
    Description: Optional[str] = None
    TimeZone: Optional[str] = None
    PrimaryChannel: Optional[str] = None
    Objective: Optional[str] = None
    PacingMode: Optional[str] = None
    
    # Features and flags
    AutoAllocatorEnabled: Optional[bool] = None
    AutoPrioritizationEnabled: Optional[bool] = None
    IncludeDefaultsFromAdvertiser: Optional[bool] = None
    
    # Related entities
    CampaignFlights: Optional[List[CampaignFlight]] = None
    NewFrequencyConfigs: Optional[List[FrequencyConfig]] = None
    AssociatedBidLists: Optional[List[BidList]] = None
    AdditionalFeeCardOnCreate: Optional[FeeCard] = None
    CurrentAndFutureAdditionalFeeCards: Optional[List[FeeCard]] = None
    
    CustomLabels: Optional[List[CustomLabel]] = None
    DefaultBidLists: Optional[List[BidList]] = None
    PurchaseOrderNumber: Optional[str] = None
    
    IsBallotMeasure: Optional[bool] = None
    BallotMeasureProfile: Optional[dict] = None
    
    CampaignConversionReportingColumns: Optional[List[dict]] = None
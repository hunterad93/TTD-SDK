from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum
from pydantic import BaseModel

from .base_types import (
    CurrencyAmount, 
    BidList, 
    FrequencyConfig, 
    Goal
)

class AdGroupCategory(BaseModel):
    CategoryId: Optional[int] = None
    CategoryName: Optional[str] = None
    CategoryTaxonomyId: Optional[int] = None
    CategoryTaxonomyName: Optional[str] = None
    CategoryTaxonomyVersion: Optional[str] = None
    Mappings: Optional[List[Dict[str, str]]] = None

class Fee(BaseModel):
    CpcRate: Optional[CurrencyAmount] = None
    CpcRateInAdvertiserCurrency: Optional[CurrencyAmount] = None
    CpmRate: Optional[CurrencyAmount] = None
    CpmRateInAdvertiserCurrency: Optional[CurrencyAmount] = None
    PercentOfDataCostRate: Optional[float] = None
    PercentOfMediaCostRate: Optional[float] = None

class AdGroupFlight(BaseModel):
    AdGroupId: Optional[str] = None
    BudgetInAdvertiserCurrency: Optional[float] = None
    BudgetInImpressions: Optional[int] = None
    CampaignFlightId: Optional[int] = None
    DailyTargetInAdvertiserCurrency: Optional[float] = None
    DailyTargetInImpressions: Optional[int] = None

class BudgetSettings(BaseModel):
    AdGroupFlights: Optional[List[AdGroupFlight]] = None
    AutoAllocatorPriority: Optional[int] = None
    Budget: Optional[CurrencyAmount] = None
    BudgetInImpressions: Optional[int] = None
    DailyBudget: Optional[CurrencyAmount] = None
    DailyBudgetInImpressions: Optional[int] = None
    PacingMode: Optional[str] = None

class CrossDeviceVendor(BaseModel):
    CrossDeviceVendorFee: Optional[Fee] = None
    CrossDeviceVendorId: Optional[int] = None
    CrossDeviceVendorName: Optional[str] = None

class AudienceRetargetingSettings(BaseModel):
    CustomizeRetargetingAudience: Optional[bool] = None
    FirstPartyDataIds: Optional[List[int]] = None

class AudienceAcceleratorExclusion(BaseModel):
    Name: Optional[str] = None
    ThirdPartyDataId: Optional[int] = None

class TargetDemographicSettings(BaseModel):
    CountryCode: Optional[str] = None
    DataRateType: Optional[str] = None
    EndAge: Optional[str] = None
    Gender: Optional[str] = None
    StartAge: Optional[str] = None

class TargetInterestSettings(BaseModel):
    CategoryId: Optional[str] = None
    CategoryName: Optional[str] = None

class AudienceTargeting(BaseModel):
    AudienceId: Optional[str] = None
    AudienceAcceleratorExclusionsEnabled: Optional[bool] = None
    AudienceBoosterEnabled: Optional[bool] = None
    AudienceExcluderEnabled: Optional[bool] = None
    AudiencePredictorEnabled: Optional[bool] = None
    AudienceRetargetingEnabled: Optional[bool] = None
    UseMcIdAsPrimary: Optional[bool] = None
    RecencyExclusionWindowInMinutes: Optional[int] = None
    TargetTrackableUsersEnabled: Optional[bool] = None
    AudienceRetargetingSettings: Optional[AudienceRetargetingSettings] = None
    CrossDeviceVendorListForAudience: Optional[List[CrossDeviceVendor]] = None
    CustomAudienceAcceleratorExclusions: Optional[List[AudienceAcceleratorExclusion]] = None
    TargetDemographicSettings: Optional[TargetDemographicSettings] = None
    TargetInterestSettings: Optional[TargetInterestSettings] = None

class RTBAttributes(BaseModel):
    AudienceTargeting: Optional[AudienceTargeting] = None
    BaseBidCpm: Optional[CurrencyAmount] = None
    BudgetSettings: Optional[BudgetSettings] = None
    CreativeIds: Optional[List[str]] = None
    MaxBidCpm: Optional[CurrencyAmount] = None
    RoiGoal: Optional[Goal] = None
    IsUseClicksAsConversionsEnabled: Optional[bool] = None
    IsUseSecondaryConversionsEnabled: Optional[bool] = None

class AdGroup(BaseModel):
    # Basic Information
    AdGroupId: Optional[str] = None
    AdGroupName: Optional[str] = None
    CampaignId: Optional[str] = None
    ChannelId: Optional[str] = None
    Description: Optional[str] = None
    
    # Status and availability
    Availability: Optional[str] = None
    IsEnabled: Optional[bool] = None
    IsHighFillRate: Optional[bool] = None
    
    # Dates
    CreatedAtUtc: Optional[datetime] = None
    
    # Settings
    BudgetingVersion: Optional[str] = None
    FunnelLocation: Optional[str] = None
    IncludeDefaultsFromCampaign: Optional[bool] = None
    MarketplaceOptOut: Optional[bool] = None
    PredictiveClearingEnabled: Optional[bool] = None
    AreFutureKoaFeaturesEnabled: Optional[bool] = None
    
    # Features
    RtbAttributes: Optional[RTBAttributes] = None
    NewFrequencyConfigs: Optional[List[FrequencyConfig]] = None
    AssociatedBidLists: Optional[List[BidList]] = None
    
    # Categories and labels
    AdGroupCategory: Optional[AdGroupCategory] = None
    CustomLabels: Optional[List[Dict[str, str]]] = None
    
    # Value added services
    EnabledValueAddedProviders: Optional[List[str]] = None
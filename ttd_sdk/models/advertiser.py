from datetime import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field

from .base_types import (
    BidList, 
    FrequencyConfig, 
    BaseCategory, 
    CustomLabel
)

class DefaultBidList(BaseModel):
    BidListId: Optional[str] = None

class AdvertiserAudienceSettings(BaseModel):
    AudienceBoosterEnabled: Optional[bool] = None
    AudienceExcluderEnabled: Optional[bool] = None

class CandidateProfile(BaseModel):
    AudienceDescription: Optional[str] = None
    CandidateName: Optional[str] = None
    DisclaimerNotice: Optional[str] = None
    ElectionState: Optional[str] = None
    FederalVerificationId: Optional[str] = None
    FileLocationInS3: Optional[str] = None
    GeoDescription: Optional[str] = None
    IsAdvertiserIec: Optional[bool] = None
    PayingEntityAddress: Optional[str] = None
    PayingEntityEmailAddress: Optional[str] = None
    PayingEntityExecutiveName: Optional[str] = None
    PayingEntityExecutiveTitle: Optional[str] = None
    PayingEntityName: Optional[str] = None
    PoliticalDataId: Optional[str] = None
    StateVerificationId: Optional[str] = None

class Advertiser(BaseModel):
    # Basic Information with aliases
    AdvertiserId: Optional[str] = None
    AdvertiserName: Optional[str] = None
    
    # Everything else in PascalCase without aliases
    AdvertiserNameDsa: Optional[str] = None
    Description: Optional[str] = None
    DomainAddress: Optional[str] = None
    PartnerId: Optional[str] = None
    
    # Status and Configuration
    Availability: Optional[str] = None
    CurrencyCode: Optional[str] = None
    Country: Optional[str] = None
    VettingStatus: Optional[str] = None
    
    # Settings
    AttributionClickLookbackWindowInSeconds: Optional[int] = None
    AttributionImpressionLookbackWindowInSeconds: Optional[int] = None
    ClickDedupWindowInSeconds: Optional[int] = None
    ConversionDedupWindowInSeconds: Optional[int] = None
    DefaultRightMediaOfferTypeId: Optional[int] = None
    IgnoreReferralUrlInConversion: Optional[bool] = None
    
    # Categories and Labels
    AdvertiserCategory: Optional[BaseCategory] = None
    CustomLabels: Optional[List[CustomLabel]] = None
    Keywords: Optional[List[str]] = None
    DataPolicies: Optional[List[str]] = None
    
    # Audience and Bidding
    AdvertiserAudienceSettings: Optional[AdvertiserAudienceSettings] = None
    AssociatedBidLists: Optional[List[BidList]] = None
    DefaultBidLists: Optional[List[DefaultBidList]] = None
    NewFrequencyConfigs: Optional[List[FrequencyConfig]] = None
    
    # Political Advertising
    IsBallotMeasure: Optional[bool] = None
    IsCandidateElection: Optional[bool] = None
    CandidateProfiles: Optional[List[CandidateProfile]] = None
    PayerNameDsa: Optional[str] = None
    
    # Additional Properties
    LogoUrl: Optional[str] = None
    Increments: Optional[List[str]] = None
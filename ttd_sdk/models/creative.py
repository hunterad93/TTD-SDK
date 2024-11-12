from datetime import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel

class Creative(BaseModel):
    # Basic Information
    CreativeId: Optional[str] = None
    CreativeName: Optional[str] = None
    CreativeType: Optional[str] = None
    AdvertiserId: Optional[str] = None
    Description: Optional[str] = None
    
    # Status and Dates
    Availability: Optional[str] = None
    CreatedAtUtc: Optional[datetime] = None
    LastUpdatedAtUtc: Optional[datetime] = None
    FlightStartDateUtc: Optional[datetime] = None
    FlightEndDateUtc: Optional[datetime] = None
    
    # Audit Information
    CreativeAuditStatuses: Optional[List[Dict]] = None
    
    # Creative Type Specific Attributes (all as dicts)
    FlashAttributes: Optional[Dict] = None
    HostedNativeAttributes: Optional[Dict] = None
    Html5Attributes: Optional[Dict] = None
    ImageAttributes: Optional[Dict] = None
    ThirdPartyHostedAudioAttributes: Optional[Dict] = None
    ThirdPartyHostedVideoAttributes: Optional[Dict] = None
    ThirdPartyTagAttributes: Optional[Dict] = None
    TradeDeskHostedAudioAttributes: Optional[Dict] = None
    TradeDeskHostedVideoAttributes: Optional[Dict] = None
    
    # Additional Settings
    PoliticalDataId: Optional[str] = None
    ShareLink: Optional[str] = None
    WillThisBeServedInChina: Optional[bool] = None
    VioohReviewRequired: Optional[bool] = None
    VioohSelectedPublisher: Optional[str] = None
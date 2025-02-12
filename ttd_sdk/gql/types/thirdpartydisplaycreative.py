from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adformat import AdFormat
    from .adgroupsconnection import AdGroupsConnection
    from .advertiser import Advertiser
    from .auditstatuses import AuditStatuses
    from .campaignsconnection import CampaignsConnection
    from .creativetagtype import CreativeTagType
    from .dynamiccreativerule import DynamicCreativeRule
    from .expandabilitysettings import ExpandabilitySettings
    from .googlevendor import GoogleVendor
    from .malwarescan import MalwareScan
    from .tmtadpolicyscan import TMTAdPolicyScan
    from .tmtmalwarescan import TMTMalwareScan


@dataclass
class ThirdPartyDisplayCreative:
    """
    None
    """
    adFormat: Optional[AdFormat]
    adGroups: Optional[AdGroupsConnection]
    adServerCreativeId: str
    adServerName: str
    adTag: str
    advertiser: Optional[Advertiser]
    approvedBy: str
    auditStatuses: Optional[AuditStatuses]
    campaigns: Optional[CampaignsConnection]
    createdAt: Any
    creativeTechVendorId: int
    description: str
    dynamicCreativeRules: List[Optional[DynamicCreativeRule]]
    expandabilitySettings: Optional[ExpandabilitySettings]
    flightEnd: Any
    flightEndDateUTC: Any
    flightStart: Any
    flightStartDateUTC: Any
    flightTimeZone: str
    flightTimeZoneIANA: Any
    googleVendors: List[Optional[GoogleVendor]]
    id: str
    idInteger: int
    interstitialSupportId: int
    isClickTrackingSuccessful: bool
    isSecurable: bool
    landingPageUrls: List[str]
    lastUpdatedAt: Any
    malwareScan: Optional[MalwareScan]
    mraidVersionId: str
    name: str
    originalAdTag: str
    pixelImpressionTrackingUrl1: str
    pixelImpressionTrackingUrl2: str
    pixelImpressionTrackingUrl3: str
    shareLink: str
    tagType: int
    tagTypeEnum: Optional[CreativeTagType]
    thirdPartyClickTrackingUrl: str
    thirdPartyTrackingTags: List[str]
    thumbnailUrl: str
    tmtAdPolicyScan: Optional[TMTAdPolicyScan]
    tmtMalwareScan: Optional[TMTMalwareScan]

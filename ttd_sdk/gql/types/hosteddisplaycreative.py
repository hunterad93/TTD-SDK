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
    from .chinacreativeinfo import ChinaCreativeInfo
    from .creativetagtype import CreativeTagType
    from .expandabilitysettings import ExpandabilitySettings
    from .googlevendor import GoogleVendor
    from .malwarescan import MalwareScan
    from .tmtadpolicyscan import TMTAdPolicyScan
    from .tmtmalwarescan import TMTMalwareScan


@dataclass
class HostedDisplayCreative:
    """
    None
    """
    adFormat: Optional[AdFormat]
    adGroups: Optional[AdGroupsConnection]
    adServerCreativeId: str
    adServerName: str
    advertiser: Optional[Advertiser]
    approvedBy: str
    auditStatuses: Optional[AuditStatuses]
    campaigns: Optional[CampaignsConnection]
    chinaCreativeInfo: Optional[ChinaCreativeInfo]
    clickthroughUrl: str
    createdAt: Any
    description: str
    enabledMiaozhenProduct: Any
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
    imageUrl: str
    interstitialSupportId: int
    isClickTrackingSuccessful: bool
    isSecurable: bool
    landingPageUrl: str
    lastUpdatedAt: Any
    malwareScan: Optional[MalwareScan]
    name: str
    pixelImpressionTrackingUrl1: str
    pixelImpressionTrackingUrl2: str
    pixelImpressionTrackingUrl3: str
    shareLink: str
    tagType: int
    tagTypeEnum: Optional[CreativeTagType]
    thirdPartyClickTrackingUrl: str
    thirdPartyTrackingTags: List[str]
    tmtAdPolicyScan: Optional[TMTAdPolicyScan]
    tmtMalwareScan: Optional[TMTMalwareScan]

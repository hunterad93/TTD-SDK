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
    from .googlevendor import GoogleVendor
    from .hostedcompanioninfo import HostedCompanionInfo
    from .hostedcreativeencodingtask import HostedCreativeEncodingTask
    from .malwarescan import MalwareScan
    from .tmtadpolicyscan import TMTAdPolicyScan
    from .tmtmalwarescan import TMTMalwareScan
    from .videoeventmodel import VideoEventModel


@dataclass
class HostedAudioCreative:
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
    clickthroughUrl: str
    companionInfo: Optional[HostedCompanionInfo]
    createdAt: Any
    daastPreviewUrl: str
    description: str
    durationInSeconds: int
    enabledMiaozhenProduct: Any
    encodingTask: Optional[HostedCreativeEncodingTask]
    flightEnd: Any
    flightEndDateUTC: Any
    flightStart: Any
    flightStartDateUTC: Any
    flightTimeZone: str
    flightTimeZoneIANA: Any
    googleVendors: List[Optional[GoogleVendor]]
    hostedCreativeEncodingTask: Optional[HostedCreativeEncodingTask]
    id: str
    idInteger: int
    interstitialSupportId: int
    isRetargetingEnabled: bool
    isSecurable: bool
    landingPageUrl: str
    lastUpdatedAt: Any
    malwareScan: Optional[MalwareScan]
    name: str
    playerTrackingEvents: List[Optional[VideoEventModel]]
    shareLink: str
    tagType: int
    tagTypeEnum: Optional[CreativeTagType]
    thirdPartyClickTrackingUrl: str
    tmtAdPolicyScan: Optional[TMTAdPolicyScan]
    tmtMalwareScan: Optional[TMTMalwareScan]
    vastPreviewUrl: str

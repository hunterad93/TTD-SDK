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
    from .crosschannelverification import CrossChannelVerification
    from .googlevendor import GoogleVendor
    from .malwarescan import MalwareScan
    from .tmtadpolicyscan import TMTAdPolicyScan
    from .tmtmalwarescan import TMTMalwareScan
    from .videoeventmodel import VideoEventModel


@dataclass
class BroadcasterHostedVideoCreative:
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
    createdAt: Any
    crossChannelVerifications: List[Optional[CrossChannelVerification]]
    description: str
    durationInSeconds: int
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
    isRetargetingEnabled: bool
    isSkippable: bool
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

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
    from .creativescanstatus import CreativeScanStatus
    from .creativetagtype import CreativeTagType
    from .crosschannelverification import CrossChannelVerification
    from .dynamiccreativerule import DynamicCreativeRule
    from .googlevendor import GoogleVendor
    from .malwarescan import MalwareScan
    from .mediafile import MediaFile
    from .tmtadpolicyscan import TMTAdPolicyScan
    from .tmtmalwarescan import TMTMalwareScan
    from .thirdpartycompanioninfo import ThirdPartyCompanionInfo
    from .thirdpartyvideovastinfo import ThirdPartyVideoVastInfo
    from .universaladid import UniversalAdId
    from .videoeventmodel import VideoEventModel


@dataclass
class ThirdPartyVideoCreative:
    """
    None
    """
    adFormat: Optional[AdFormat]
    adGroups: Optional[AdGroupsConnection]
    adServerCreativeId: str
    adServerName: str
    adTagUrl: str
    advertiser: Optional[Advertiser]
    approvedBy: str
    auditStatuses: Optional[AuditStatuses]
    campaigns: Optional[CampaignsConnection]
    clickthroughUrl: str
    companionInfo: Optional[ThirdPartyCompanionInfo]
    createdAt: Any
    creativeScanStatus: Optional[CreativeScanStatus]
    crossChannelVerifications: List[Optional[CrossChannelVerification]]
    description: str
    durationInSeconds: int
    dynamicCreativeRules: List[Optional[DynamicCreativeRule]]
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
    isSecurable: bool
    isSkippable: bool
    isVideoMeasurementEnabled: bool
    isVideoRetargetingEnabled: bool
    landingPageUrl: str
    lastUpdatedAt: Any
    malwareScan: Optional[MalwareScan]
    mediaFiles: List[Optional[MediaFile]]
    name: str
    scanStatus: Optional[CreativeScanStatus]
    shareLink: str
    skipOffsetInSeconds: int
    tagType: int
    tagTypeEnum: Optional[CreativeTagType]
    thirdPartyClickTrackingUrl: str
    tmtAdPolicyScan: Optional[TMTAdPolicyScan]
    tmtMalwareScan: Optional[TMTMalwareScan]
    trackingEvents: List[Optional[VideoEventModel]]
    universalAdId: Optional[UniversalAdId]
    vastInfo: Optional[ThirdPartyVideoVastInfo]
    vastPreviewUrl: str
    vastTag: str

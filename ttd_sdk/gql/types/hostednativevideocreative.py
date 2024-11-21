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
    from .creativeimageassets import CreativeImageAssets
    from .creativetagtype import CreativeTagType
    from .creativetextassets import CreativeTextAssets
    from .creativevideoasset import CreativeVideoAsset
    from .crosschannelverification import CrossChannelVerification
    from .googlevendor import GoogleVendor
    from .hostedcreativeencodingtask import HostedCreativeEncodingTask
    from .malwarescan import MalwareScan
    from .tmtadpolicyscan import TMTAdPolicyScan
    from .tmtmalwarescan import TMTMalwareScan
    from .videoeventmodel import VideoEventModel


@dataclass
class HostedNativeVideoCreative:
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
    crossChannelVerifications: List[Optional[CrossChannelVerification]]
    description: str
    durationInSeconds: int
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
    images: Optional[CreativeImageAssets]
    interstitialSupportId: int
    isClickTrackingSuccessful: bool
    isRetargetingEnabled: bool
    landingPageUrl: str
    lastUpdatedAt: Any
    malwareScan: Optional[MalwareScan]
    name: str
    pixelImpressionTrackingUrl1: str
    pixelImpressionTrackingUrl2: str
    pixelImpressionTrackingUrl3: str
    playerTrackingEvents: List[Optional[VideoEventModel]]
    rating: Any
    shareLink: str
    tagType: int
    tagTypeEnum: Optional[CreativeTagType]
    texts: Optional[CreativeTextAssets]
    thirdPartyClickTrackingUrl: str
    tmtAdPolicyScan: Optional[TMTAdPolicyScan]
    tmtMalwareScan: Optional[TMTMalwareScan]
    vastPreviewUrl: str
    videos: List[Optional[CreativeVideoAsset]]

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser
    from .campaign import Campaign
    from .conversionliftcrossdevicevendor import ConversionLiftCrossDeviceVendor
    from .conversionliftofflinedataprovider import ConversionLiftOfflineDataProvider
    from .conversionliftpostexperimentconversionwindowindays import ConversionLiftPostExperimentConversionWindowInDays
    from .conversionliftprovidername import ConversionLiftProviderName
    from .conversionliftstudystatus import ConversionLiftStudyStatus
    from .trackingtag import TrackingTag


@dataclass
class ConversionLiftExperiment:
    """
    None
    """
    advertiser: Optional[Advertiser]
    attributionWindow: Any
    campaigns: List[Optional[Campaign]]
    conversionIds: List[str]
    createdAtUtc: Any
    crossDeviceVendorId: Optional[ConversionLiftCrossDeviceVendor]
    emailAddress: str
    endDate: Any
    estimatedMinimumImpressions: int
    experimentName: str
    holdoutRate: Any
    id: str
    itemSets: List[str]
    lastUpdatedAtUtc: Any
    liftStudyProviderName: Optional[ConversionLiftProviderName]
    offlineDataProvider: Optional[ConversionLiftOfflineDataProvider]
    postExperimentConversionCampaignInDays: Optional[ConversionLiftPostExperimentConversionWindowInDays]
    primaryTrackTag: Optional[TrackingTag]
    startDate: Any
    status: Optional[ConversionLiftStudyStatus]

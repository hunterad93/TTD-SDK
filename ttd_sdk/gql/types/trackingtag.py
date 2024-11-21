from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser
    from .dataeventtype import DataEventType
    from .firstpartydata import FirstPartyData
    from .offlinedataprovider import OfflineDataProvider
    from .trackingtagcategory import TrackingTagCategory
    from .trackingtagtype import TrackingTagType
    from .universalpixel import UniversalPixel


@dataclass
class TrackingTag:
    """
    None
    """
    advertiser: Optional[Advertiser]
    category: Optional[TrackingTagCategory]
    containerTagBody: str
    currency: str
    dataEventType: Optional[DataEventType]
    firstPartyData: Optional[FirstPartyData]
    hitCount1Day: int
    hitCount30Day: int
    hitCount7Day: int
    householdEnabled: bool
    id: str
    iFrameTag: str
    imageTag: str
    isArchived: bool
    location: str
    name: str
    offlineDataProvider: Optional[OfflineDataProvider]
    redirectUri: str
    revenue: str
    type: Optional[TrackingTagType]
    universalPixel: Optional[UniversalPixel]

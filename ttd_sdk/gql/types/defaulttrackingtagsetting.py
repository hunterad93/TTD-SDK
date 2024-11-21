from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .defaulttrackingsupportedcreativetype import DefaultTrackingSupportedCreativeType
    from .trackingurloptions import TrackingUrlOptions


@dataclass
class DefaultTrackingTagSetting:
    """
    None
    """
    advertiserDefault: str
    creativeTypes: List[Optional[DefaultTrackingSupportedCreativeType]]
    partnerDefault: str
    selectedTrackingType: Optional[TrackingUrlOptions]

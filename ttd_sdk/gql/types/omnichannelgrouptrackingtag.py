from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .crossdeviceattribution import CrossDeviceAttribution
    from .trackingtag import TrackingTag


@dataclass
class OmnichannelGroupTrackingTag:
    """
    A tracking tag and cross-device attribution model pair for an omnichannel group.
    """
    crossDeviceAttributionModel: Optional[CrossDeviceAttribution]
    omnichannelGroupId: int
    trackingTag: Optional[TrackingTag]

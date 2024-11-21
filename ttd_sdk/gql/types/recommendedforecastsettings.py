from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupfunnellocationtype import AdGroupFunnelLocationType
    from .inventorychanneltype import InventoryChannelType
    from .roigoaltype import ROIGoalType


@dataclass
class RecommendedForecastSettings:
    """
    Recommended forecast settings.
    """
    adGroupFunnelLocationType: Optional[AdGroupFunnelLocationType]
    channel: Optional[InventoryChannelType]
    cpmInAdvertiserCurrency: Any
    roiGoal: Optional[ROIGoalType]

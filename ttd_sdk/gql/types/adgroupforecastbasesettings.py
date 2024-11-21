from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adformatduration import AdFormatDuration
    from .adformatfiletype import AdFormatFileType
    from .adgroupforecastbidlist import AdGroupForecastBidList
    from .adgroupfunnellocationtype import AdGroupFunnelLocationType
    from .audience import Audience
    from .frequencycap import FrequencyCap
    from .inventorychannel import InventoryChannel
    from .markettype import MarketType
    from .roigoaltype import ROIGoalType
    from .seed import Seed


@dataclass
class AdGroupForecastBaseSettings:
    """
    Settings for an ad group level forecast
    """
    adFormatDurations: List[Optional[AdFormatDuration]]
    adFormatFileTypes: List[Optional[AdFormatFileType]]
    adGroupFunnelLocationType: Optional[AdGroupFunnelLocationType]
    audience: Optional[Audience]
    bidLists: List[Optional[AdGroupForecastBidList]]
    budgetInAdvertiserCurrency: Any
    channel: Optional[InventoryChannel]
    forecastDurationInDays: int
    frequencyCap: Optional[FrequencyCap]
    isPolitical: bool
    marketType: Optional[MarketType]
    qualityAllianceViewabilityProfile: int
    roiGoal: Optional[ROIGoalType]
    seed: Optional[Seed]
    targetAllKnowUsers: bool

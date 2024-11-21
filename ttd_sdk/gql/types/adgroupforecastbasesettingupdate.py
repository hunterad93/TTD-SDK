from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adformatdurationupdate import AdFormatDurationUpdate
    from .adformatfiletypeupdate import AdFormatFileTypeUpdate
    from .adgroupforecastbidlistupdate import AdGroupForecastBidListUpdate
    from .adgroupfunnellocationtype import AdGroupFunnelLocationType
    from .frequencycap import FrequencyCap
    from .inventorychannel import InventoryChannel
    from .markettype import MarketType
    from .roigoaltype import ROIGoalType
    from .seed import Seed


@dataclass
class AdGroupForecastBaseSettingUpdate:
    """
    None
    """
    adFormatDurationIds: List[Optional[AdFormatDurationUpdate]]
    adFormatFileTypeIds: List[Optional[AdFormatFileTypeUpdate]]
    adGroupFunnelLocationType: Optional[AdGroupFunnelLocationType]
    audienceId: str
    bidLists: List[Optional[AdGroupForecastBidListUpdate]]
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

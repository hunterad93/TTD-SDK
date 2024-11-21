from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupforecastbasesettings import AdGroupForecastBaseSettings
    from .adgrouplevelforecastresults import AdGroupLevelForecastResults
    from .advertiser import Advertiser
    from .forecaststatus import ForecastStatus
    from .moneymodel import MoneyModel
    from .reachtype import ReachType


@dataclass
class Forecast:
    """
    Forecast model with its settings and results
    """
    adGroupForecastSettings: Optional[AdGroupForecastBaseSettings]
    adGroupLevelForecastResults: Optional[AdGroupLevelForecastResults]
    advertiser: Optional[Advertiser]
    cpm: Optional[MoneyModel]
    createdByUser: str
    id: str
    isArchived: bool
    isAsync: bool
    lastUpdatedByUser: str
    name: str
    reachType: Optional[ReachType]
    status: Optional[ForecastStatus]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupforecastbasesettingupdate import AdGroupForecastBaseSettingUpdate
    from .moneymodel import MoneyModel
    from .reachtype import ReachType


@dataclass
class ForecastSettingsUpdate:
    """
    None
    """
    cpm: Optional[MoneyModel]
    forecastId: int
    isArchived: bool
    name: str
    reachType: Optional[ReachType]
    updatedForecastSettings: Optional[AdGroupForecastBaseSettingUpdate]

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .baseforecastingcurvedatapoint import BaseForecastingCurveDataPoint
    from .forecastingcurvedatapoint import ForecastingCurveDataPoint


@dataclass
class AdGroupLevelForecastResults:
    """
    None
    """
    availsNumber: int
    curves: List[Optional[ForecastingCurveDataPoint]]
    durationInDays: int
    lastCalculatedAt: Any
    maxPotentialSpend: int
    spend: int
    valuesAtInputBudget: Optional[BaseForecastingCurveDataPoint]

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .forecast import Forecast
    from .forecastsforadvertiseredge import ForecastsForAdvertiserEdge
    from .pageinfo import PageInfo


@dataclass
class ForecastsForAdvertiserConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ForecastsForAdvertiserEdge]]
    nodes: List[Optional[Forecast]]
    pageInfo: Optional[PageInfo]
    totalCount: int

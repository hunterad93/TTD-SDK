from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .forecast import Forecast


@dataclass
class ForecastsForAdvertiserEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[Forecast]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupflight import AdGroupFlight


@dataclass
class AdGroupFlightsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[AdGroupFlight]

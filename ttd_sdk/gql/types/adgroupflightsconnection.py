from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupflight import AdGroupFlight
    from .adgroupflightsedge import AdGroupFlightsEdge
    from .pageinfo import PageInfo


@dataclass
class AdGroupFlightsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AdGroupFlightsEdge]]
    nodes: List[Optional[AdGroupFlight]]
    pageInfo: Optional[PageInfo]
    totalCount: int

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignflight import CampaignFlight
    from .flightsedge import FlightsEdge
    from .pageinfo import PageInfo


@dataclass
class FlightsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[FlightsEdge]]
    nodes: List[Optional[CampaignFlight]]
    pageInfo: Optional[PageInfo]
    totalCount: int

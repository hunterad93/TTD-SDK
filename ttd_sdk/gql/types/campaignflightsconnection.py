from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignflight import CampaignFlight
    from .campaignflightsedge import CampaignFlightsEdge
    from .pageinfo import PageInfo


@dataclass
class CampaignFlightsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[CampaignFlightsEdge]]
    nodes: List[Optional[CampaignFlight]]
    pageInfo: Optional[PageInfo]
    totalCount: int

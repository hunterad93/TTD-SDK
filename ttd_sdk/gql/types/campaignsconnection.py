from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaign import Campaign
    from .campaignsedge import CampaignsEdge
    from .pageinfo import PageInfo


@dataclass
class CampaignsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[CampaignsEdge]]
    nodes: List[Optional[Campaign]]
    pageInfo: Optional[PageInfo]
    totalCount: int

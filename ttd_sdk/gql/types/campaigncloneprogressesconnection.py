from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaigncloneprogress import CampaignCloneProgress
    from .campaigncloneprogressesedge import CampaignCloneProgressesEdge
    from .pageinfo import PageInfo


@dataclass
class CampaignCloneProgressesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[CampaignCloneProgressesEdge]]
    nodes: List[Optional[CampaignCloneProgress]]
    pageInfo: Optional[PageInfo]
    totalCount: int

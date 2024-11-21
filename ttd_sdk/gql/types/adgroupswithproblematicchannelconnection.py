from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup
    from .adgroupswithproblematicchanneledge import AdGroupsWithProblematicChannelEdge
    from .pageinfo import PageInfo


@dataclass
class AdGroupsWithProblematicChannelConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AdGroupsWithProblematicChannelEdge]]
    nodes: List[Optional[AdGroup]]
    pageInfo: Optional[PageInfo]
    totalCount: int

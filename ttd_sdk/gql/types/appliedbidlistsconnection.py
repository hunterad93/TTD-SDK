from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .appliedbidlistsedge import AppliedBidListsEdge
    from .ibidlist import IBidList
    from .pageinfo import PageInfo


@dataclass
class AppliedBidListsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AppliedBidListsEdge]]
    nodes: List[Optional[IBidList]]
    pageInfo: Optional[PageInfo]
    totalCount: int

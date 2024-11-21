from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .defaultbidlistsedge import DefaultBidListsEdge
    from .ibidlist import IBidList
    from .pageinfo import PageInfo


@dataclass
class DefaultBidListsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[DefaultBidListsEdge]]
    nodes: List[Optional[IBidList]]
    pageInfo: Optional[PageInfo]
    totalCount: int

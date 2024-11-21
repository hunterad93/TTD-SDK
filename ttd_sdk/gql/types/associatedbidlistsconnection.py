from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .associatedbidlist import AssociatedBidList
    from .associatedbidlistsedge import AssociatedBidListsEdge
    from .pageinfo import PageInfo


@dataclass
class AssociatedBidListsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AssociatedBidListsEdge]]
    nodes: List[Optional[AssociatedBidList]]
    pageInfo: Optional[PageInfo]
    totalCount: int

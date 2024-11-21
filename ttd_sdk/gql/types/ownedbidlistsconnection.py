from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ibidlist import IBidList
    from .ownedbidlistsedge import OwnedBidListsEdge
    from .pageinfo import PageInfo


@dataclass
class OwnedBidListsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[OwnedBidListsEdge]]
    nodes: List[Optional[IBidList]]
    pageInfo: Optional[PageInfo]
    totalCount: int

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupassociatedbidlist import AdGroupAssociatedBidList
    from .adgroupassociatedbidlistsedge import AdGroupAssociatedBidListsEdge
    from .pageinfo import PageInfo


@dataclass
class AdGroupAssociatedBidListsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AdGroupAssociatedBidListsEdge]]
    nodes: List[Optional[AdGroupAssociatedBidList]]
    pageInfo: Optional[PageInfo]
    totalCount: int

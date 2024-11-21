from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .dealsedge import DealsEdge
    from .pageinfo import PageInfo
    from .privatecontract import PrivateContract


@dataclass
class DealsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[DealsEdge]]
    nodes: List[Optional[PrivateContract]]
    pageInfo: Optional[PageInfo]
    totalCount: int

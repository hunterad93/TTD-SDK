from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .passthroughfee import PassThroughFee
    from .passthroughfeesedge import PassThroughFeesEdge


@dataclass
class PassThroughFeesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PassThroughFeesEdge]]
    nodes: List[Optional[PassThroughFee]]
    pageInfo: Optional[PageInfo]
    totalCount: int

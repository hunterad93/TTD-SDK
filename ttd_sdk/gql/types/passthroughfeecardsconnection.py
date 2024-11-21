from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .passthroughfeecard import PassThroughFeeCard
    from .passthroughfeecardsedge import PassThroughFeeCardsEdge


@dataclass
class PassThroughFeeCardsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PassThroughFeeCardsEdge]]
    nodes: List[Optional[PassThroughFeeCard]]
    pageInfo: Optional[PageInfo]
    totalCount: int

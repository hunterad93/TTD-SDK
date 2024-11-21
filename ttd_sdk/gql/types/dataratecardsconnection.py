from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .dataratecard import DataRateCard
    from .dataratecardsedge import DataRateCardsEdge
    from .pageinfo import PageInfo


@dataclass
class DataRateCardsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[DataRateCardsEdge]]
    nodes: List[Optional[DataRateCard]]
    pageInfo: Optional[PageInfo]
    totalCount: int

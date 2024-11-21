from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .datarate import DataRate
    from .dataratesedge import DataRatesEdge
    from .pageinfo import PageInfo


@dataclass
class DataRatesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[DataRatesEdge]]
    nodes: List[Optional[DataRate]]
    pageInfo: Optional[PageInfo]
    totalCount: int

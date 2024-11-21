from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .publisherpropertyspend import PublisherPropertySpend
    from .spendedge import SpendEdge


@dataclass
class SpendConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[SpendEdge]]
    nodes: List[Optional[PublisherPropertySpend]]
    pageInfo: Optional[PageInfo]
    totalCount: int

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .universalpixel import UniversalPixel
    from .universalpixelsedge import UniversalPixelsEdge


@dataclass
class UniversalPixelsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[UniversalPixelsEdge]]
    nodes: List[Optional[UniversalPixel]]
    pageInfo: Optional[PageInfo]
    totalCount: int

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .geosegment import GeoSegment
    from .geosegmentssearchedge import GeoSegmentsSearchEdge
    from .pageinfo import PageInfo


@dataclass
class GeoSegmentsSearchConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[GeoSegmentsSearchEdge]]
    nodes: List[Optional[GeoSegment]]
    pageInfo: Optional[PageInfo]
    totalCount: int

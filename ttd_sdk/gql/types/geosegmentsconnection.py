from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .geosegment import GeoSegment
    from .geosegmentsedge import GeoSegmentsEdge
    from .pageinfo import PageInfo


@dataclass
class GeoSegmentsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[GeoSegmentsEdge]]
    nodes: List[Optional[GeoSegment]]
    pageInfo: Optional[PageInfo]
    totalCount: int

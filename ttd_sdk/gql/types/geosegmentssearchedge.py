from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .geosegment import GeoSegment


@dataclass
class GeoSegmentsSearchEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[GeoSegment]

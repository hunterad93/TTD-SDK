from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .trackingtag import TrackingTag
    from .trackingtagsedge import TrackingTagsEdge


@dataclass
class TrackingTagsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[TrackingTagsEdge]]
    nodes: List[Optional[TrackingTag]]
    pageInfo: Optional[PageInfo]
    totalCount: int

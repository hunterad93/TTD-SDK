from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .universalpixeltrackingtag import UniversalPixelTrackingTag
    from .universalpixeltrackingtagsedge import UniversalPixelTrackingTagsEdge


@dataclass
class UniversalPixelTrackingTagsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[UniversalPixelTrackingTagsEdge]]
    nodes: List[Optional[UniversalPixelTrackingTag]]
    pageInfo: Optional[PageInfo]
    totalCount: int

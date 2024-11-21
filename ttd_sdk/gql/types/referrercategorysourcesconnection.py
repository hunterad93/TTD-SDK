from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .referrercategorysource import ReferrerCategorySource
    from .referrercategorysourcesedge import ReferrerCategorySourcesEdge


@dataclass
class ReferrerCategorySourcesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ReferrerCategorySourcesEdge]]
    nodes: List[Optional[ReferrerCategorySource]]
    pageInfo: Optional[PageInfo]
    totalCount: int

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .prebidcontextualcategoriesedge import PreBidContextualCategoriesEdge
    from .prebidcontextualcategory import PreBidContextualCategory


@dataclass
class PreBidContextualCategoriesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PreBidContextualCategoriesEdge]]
    nodes: List[Optional[PreBidContextualCategory]]
    pageInfo: Optional[PageInfo]
    totalCount: int

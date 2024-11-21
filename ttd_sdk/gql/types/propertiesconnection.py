from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .propertiesedge import PropertiesEdge
    from .recommendedproperty import RecommendedProperty


@dataclass
class PropertiesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PropertiesEdge]]
    nodes: List[Optional[RecommendedProperty]]
    pageInfo: Optional[PageInfo]
    totalCount: int

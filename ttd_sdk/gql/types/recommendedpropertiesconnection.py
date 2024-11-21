from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .publisherproperty import PublisherProperty
    from .recommendedpropertiesedge import RecommendedPropertiesEdge


@dataclass
class RecommendedPropertiesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[RecommendedPropertiesEdge]]
    nodes: List[Optional[PublisherProperty]]
    pageInfo: Optional[PageInfo]
    totalCount: int

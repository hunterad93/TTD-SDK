from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualentitiesedge import ContextualEntitiesEdge
    from .contextualentity import ContextualEntity
    from .pageinfo import PageInfo


@dataclass
class ContextualEntitiesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ContextualEntitiesEdge]]
    nodes: List[Optional[ContextualEntity]]
    pageInfo: Optional[PageInfo]
    totalCount: int

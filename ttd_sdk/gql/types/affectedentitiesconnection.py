from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .affectedentitiesedge import AffectedEntitiesEdge
    from .affectedentitytype import AffectedEntityType
    from .pageinfo import PageInfo


@dataclass
class AffectedEntitiesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AffectedEntitiesEdge]]
    nodes: List[Optional[AffectedEntityType]]
    pageInfo: Optional[PageInfo]
    totalCount: int

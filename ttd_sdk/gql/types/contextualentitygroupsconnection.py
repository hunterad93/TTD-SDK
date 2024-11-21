from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualentitygroup import ContextualEntityGroup
    from .contextualentitygroupsedge import ContextualEntityGroupsEdge
    from .pageinfo import PageInfo


@dataclass
class ContextualEntityGroupsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ContextualEntityGroupsEdge]]
    nodes: List[Optional[ContextualEntityGroup]]
    pageInfo: Optional[PageInfo]
    totalCount: int

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualentitygroupmapping import ContextualEntityGroupMapping
    from .contextualentitygroupmappingsedge import ContextualEntityGroupMappingsEdge
    from .pageinfo import PageInfo


@dataclass
class ContextualEntityGroupMappingsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ContextualEntityGroupMappingsEdge]]
    nodes: List[Optional[ContextualEntityGroupMapping]]
    pageInfo: Optional[PageInfo]
    totalCount: int

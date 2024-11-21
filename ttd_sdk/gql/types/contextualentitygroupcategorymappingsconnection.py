from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualentitygroupcategorymapping import ContextualEntityGroupCategoryMapping
    from .contextualentitygroupcategorymappingsedge import ContextualEntityGroupCategoryMappingsEdge
    from .pageinfo import PageInfo


@dataclass
class ContextualEntityGroupCategoryMappingsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ContextualEntityGroupCategoryMappingsEdge]]
    nodes: List[Optional[ContextualEntityGroupCategoryMapping]]
    pageInfo: Optional[PageInfo]
    totalCount: int

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualentitygroupcategorymappingsconnection import ContextualEntityGroupCategoryMappingsConnection
    from .prebidcontextualentitygroupstate import PreBidContextualEntityGroupState
    from .prebidcontextualentitygrouptype import PreBidContextualEntityGroupType


@dataclass
class ContextualEntityGroup:
    """
    Represents a contextual entity group in the contextual marketplace.
    """
    contextualEntityGroupCategoryMappings: Optional[ContextualEntityGroupCategoryMappingsConnection]
    createdAt: Any
    description: str
    groupType: Optional[PreBidContextualEntityGroupType]
    id: str
    name: str
    state: Optional[PreBidContextualEntityGroupState]

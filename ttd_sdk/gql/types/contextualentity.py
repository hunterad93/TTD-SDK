from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualentitygroupmappingsconnection import ContextualEntityGroupMappingsConnection
    from .contextualentitysource import ContextualEntitySource
    from .contextualentitystate import ContextualEntityState


@dataclass
class ContextualEntity:
    """
    Represents a contextual entity in the contextual marketplace.
    """
    clonedFromContextualId: str
    contextualEntityGroupMappings: Optional[ContextualEntityGroupMappingsConnection]
    createdAt: Any
    id: str
    name: str
    source: Optional[ContextualEntitySource]
    state: Optional[ContextualEntityState]

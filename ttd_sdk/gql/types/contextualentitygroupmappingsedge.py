from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualentitygroupmapping import ContextualEntityGroupMapping


@dataclass
class ContextualEntityGroupMappingsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[ContextualEntityGroupMapping]

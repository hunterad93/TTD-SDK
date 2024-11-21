from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualentitygroup import ContextualEntityGroup


@dataclass
class ContextualEntityGroupsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[ContextualEntityGroup]

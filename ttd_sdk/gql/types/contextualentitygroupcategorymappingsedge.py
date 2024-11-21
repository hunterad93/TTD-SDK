from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualentitygroupcategorymapping import ContextualEntityGroupCategoryMapping


@dataclass
class ContextualEntityGroupCategoryMappingsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[ContextualEntityGroupCategoryMapping]

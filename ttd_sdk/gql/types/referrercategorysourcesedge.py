from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .referrercategorysource import ReferrerCategorySource


@dataclass
class ReferrerCategorySourcesEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[ReferrerCategorySource]

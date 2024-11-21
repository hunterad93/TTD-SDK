from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .prebidcontextualcategory import PreBidContextualCategory


@dataclass
class PreBidContextualCategoriesEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[PreBidContextualCategory]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .recommendedproperty import RecommendedProperty


@dataclass
class PropertiesEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[RecommendedProperty]
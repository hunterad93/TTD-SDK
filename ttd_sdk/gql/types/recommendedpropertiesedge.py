from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .publisherproperty import PublisherProperty


@dataclass
class RecommendedPropertiesEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[PublisherProperty]

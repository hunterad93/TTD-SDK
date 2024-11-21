from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .affectedentitytype import AffectedEntityType


@dataclass
class AffectedEntitiesEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[AffectedEntityType]

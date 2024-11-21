from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .permission import Permission


@dataclass
class PermissionsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[Permission]

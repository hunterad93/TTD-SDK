from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .permissiongroup import PermissionGroup


@dataclass
class UserAssignedPermissionGroupsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[PermissionGroup]

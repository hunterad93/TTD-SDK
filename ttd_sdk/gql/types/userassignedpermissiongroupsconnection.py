from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .permissiongroup import PermissionGroup
    from .userassignedpermissiongroupsedge import UserAssignedPermissionGroupsEdge


@dataclass
class UserAssignedPermissionGroupsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[UserAssignedPermissionGroupsEdge]]
    nodes: List[Optional[PermissionGroup]]
    pageInfo: Optional[PageInfo]
    totalCount: int

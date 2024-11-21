from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .assignedpermissiongroupsedge import AssignedPermissionGroupsEdge
    from .pageinfo import PageInfo
    from .permissiongroup import PermissionGroup


@dataclass
class AssignedPermissionGroupsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AssignedPermissionGroupsEdge]]
    nodes: List[Optional[PermissionGroup]]
    pageInfo: Optional[PageInfo]
    totalCount: int

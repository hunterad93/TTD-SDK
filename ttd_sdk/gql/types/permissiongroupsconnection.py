from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .permissiongroup import PermissionGroup
    from .permissiongroupsedge import PermissionGroupsEdge


@dataclass
class PermissionGroupsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PermissionGroupsEdge]]
    nodes: List[Optional[PermissionGroup]]
    pageInfo: Optional[PageInfo]
    totalCount: int

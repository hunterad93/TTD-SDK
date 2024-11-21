from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .permission import Permission
    from .userassignedpermissionsedge import UserAssignedPermissionsEdge


@dataclass
class UserAssignedPermissionsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[UserAssignedPermissionsEdge]]
    nodes: List[Optional[Permission]]
    pageInfo: Optional[PageInfo]
    totalCount: int

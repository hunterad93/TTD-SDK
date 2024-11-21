from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .assignedpermissionsedge import AssignedPermissionsEdge
    from .pageinfo import PageInfo
    from .permission import Permission


@dataclass
class AssignedPermissionsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AssignedPermissionsEdge]]
    nodes: List[Optional[Permission]]
    pageInfo: Optional[PageInfo]
    totalCount: int

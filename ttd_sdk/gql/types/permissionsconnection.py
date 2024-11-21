from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .permission import Permission
    from .permissionsedge import PermissionsEdge


@dataclass
class PermissionsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PermissionsEdge]]
    nodes: List[Optional[Permission]]
    pageInfo: Optional[PageInfo]
    totalCount: int

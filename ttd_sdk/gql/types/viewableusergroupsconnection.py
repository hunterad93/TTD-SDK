from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .usergroup import UserGroup
    from .viewableusergroupsedge import ViewableUserGroupsEdge


@dataclass
class ViewableUserGroupsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ViewableUserGroupsEdge]]
    nodes: List[Optional[UserGroup]]
    pageInfo: Optional[PageInfo]
    totalCount: int

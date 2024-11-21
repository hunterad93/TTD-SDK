from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .usergroup import UserGroup


@dataclass
class ViewableUserGroupsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[UserGroup]

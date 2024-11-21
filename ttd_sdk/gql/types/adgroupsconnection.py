from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup
    from .adgroupsedge import AdGroupsEdge
    from .pageinfo import PageInfo


@dataclass
class AdGroupsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AdGroupsEdge]]
    nodes: List[Optional[AdGroup]]
    pageInfo: Optional[PageInfo]
    totalCount: int

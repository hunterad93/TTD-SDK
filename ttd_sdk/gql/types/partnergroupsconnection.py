from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .partnergroup import PartnerGroup
    from .partnergroupsedge import PartnerGroupsEdge


@dataclass
class PartnerGroupsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PartnerGroupsEdge]]
    nodes: List[Optional[PartnerGroup]]
    pageInfo: Optional[PageInfo]
    totalCount: int

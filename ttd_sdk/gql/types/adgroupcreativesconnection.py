from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupcreativesedge import AdGroupCreativesEdge
    from .creative import Creative
    from .pageinfo import PageInfo


@dataclass
class AdGroupCreativesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AdGroupCreativesEdge]]
    nodes: List[Optional[Creative]]
    pageInfo: Optional[PageInfo]
    totalCount: int

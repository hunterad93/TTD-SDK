from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .companioncreativesedge import CompanionCreativesEdge
    from .creative import Creative
    from .pageinfo import PageInfo


@dataclass
class CompanionCreativesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[CompanionCreativesEdge]]
    nodes: List[Optional[Creative]]
    pageInfo: Optional[PageInfo]
    totalCount: int

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creative import Creative
    from .creativesedge import CreativesEdge
    from .pageinfo import PageInfo


@dataclass
class CreativesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[CreativesEdge]]
    nodes: List[Optional[Creative]]
    pageInfo: Optional[PageInfo]
    totalCount: int

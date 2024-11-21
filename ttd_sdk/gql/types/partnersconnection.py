from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .partner import Partner
    from .partnersedge import PartnersEdge


@dataclass
class PartnersConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PartnersEdge]]
    nodes: List[Optional[Partner]]
    pageInfo: Optional[PageInfo]
    totalCount: int

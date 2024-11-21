from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .audience import Audience
    from .audiencesedge import AudiencesEdge
    from .pageinfo import PageInfo


@dataclass
class AudiencesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AudiencesEdge]]
    nodes: List[Optional[Audience]]
    pageInfo: Optional[PageInfo]
    totalCount: int

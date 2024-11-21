from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creativeissue import CreativeIssue
    from .creativeissuesedge import CreativeIssuesEdge
    from .pageinfo import PageInfo


@dataclass
class CreativeIssuesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[CreativeIssuesEdge]]
    nodes: List[Optional[CreativeIssue]]
    pageInfo: Optional[PageInfo]
    totalCount: int

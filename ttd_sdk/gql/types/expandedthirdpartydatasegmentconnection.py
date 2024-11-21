from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .expandedthirdpartydatasegment import ExpandedThirdPartyDataSegment
    from .expandedthirdpartydatasegmentedge import ExpandedThirdPartyDataSegmentEdge
    from .pageinfo import PageInfo


@dataclass
class ExpandedThirdPartyDataSegmentConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ExpandedThirdPartyDataSegmentEdge]]
    nodes: List[Optional[ExpandedThirdPartyDataSegment]]
    pageInfo: Optional[PageInfo]
    totalCount: int

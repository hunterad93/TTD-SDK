from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .expandedthirdpartydatasegment import ExpandedThirdPartyDataSegment


@dataclass
class ExpandedThirdPartyDataSegmentEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[ExpandedThirdPartyDataSegment]

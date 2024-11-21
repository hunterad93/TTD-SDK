from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .frequencycounter import FrequencyCounter
    from .impressionfrequencycountersedge import ImpressionFrequencyCountersEdge
    from .pageinfo import PageInfo


@dataclass
class ImpressionFrequencyCountersConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ImpressionFrequencyCountersEdge]]
    nodes: List[Optional[FrequencyCounter]]
    pageInfo: Optional[PageInfo]
    totalCount: int

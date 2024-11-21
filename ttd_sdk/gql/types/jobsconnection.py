from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignclonejob import CampaignCloneJob
    from .jobsedge import JobsEdge
    from .pageinfo import PageInfo


@dataclass
class JobsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[JobsEdge]]
    nodes: List[Optional[CampaignCloneJob]]
    pageInfo: Optional[PageInfo]
    totalCount: int

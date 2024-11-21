from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignclonejob import CampaignCloneJob


@dataclass
class JobsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[CampaignCloneJob]

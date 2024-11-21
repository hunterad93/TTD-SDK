from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaign import Campaign
    from .clonejobstatus import CloneJobStatus
    from .jobsconnection import JobsConnection


@dataclass
class CampaignCloneProgress:
    """
    None
    """
    cloneCount: int
    id: int
    jobs: Optional[JobsConnection]
    sourceCampaign: Optional[Campaign]
    status: Optional[CloneJobStatus]

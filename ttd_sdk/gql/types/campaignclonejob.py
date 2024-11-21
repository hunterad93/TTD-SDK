from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupclonefailurepairing import AdGroupCloneFailurePairing
    from .clonejobstatus import CloneJobStatus
    from .clonedcampaigninfo import ClonedCampaignInfo


@dataclass
class CampaignCloneJob:
    """
    Represents a single Campaign clone job's state.
    """
    cloneInfo: Optional[ClonedCampaignInfo]
    cloneReport: List[str]
    failedAdGroups: List[Optional[AdGroupCloneFailurePairing]]
    failureMessage: str
    id: int
    progressPercentage: float
    status: Optional[CloneJobStatus]

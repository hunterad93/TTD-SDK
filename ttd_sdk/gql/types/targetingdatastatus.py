from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .targetingdatastate import TargetingDataState


@dataclass
class TargetingDataStatus:
    """
    None
    """
    activeCounts: int
    id: str
    lastUpdatedAt: Any
    receivedCounts: int
    state: Optional[TargetingDataState]

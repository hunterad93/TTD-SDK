from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .targetingdata import TargetingData


@dataclass
class TargetingDataUniques:
    """
    None
    """
    lastUpdatedAt: Any
    targetingData: Optional[TargetingData]
    targetingDataId: str
    uniques: int
    uniquesConnectedTv: int
    uniquesInApp: int
    uniquesWeb: int
    uniquesWithThirdPartyOverlap: int

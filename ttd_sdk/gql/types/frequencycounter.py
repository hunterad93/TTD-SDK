from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .frequencycounterincrementor import FrequencyCounterIncrementor
    from .frequencycounterowner import FrequencyCounterOwner
    from .frequencycounterspecialtype import FrequencyCounterSpecialType


@dataclass
class FrequencyCounter:
    """
    None
    """
    id: str
    counterAttribute: Optional[FrequencyCounterSpecialType]
    frequencyCounterIncrementors: List[Optional[FrequencyCounterIncrementor]]
    isCustomName: bool
    isDeleted: bool
    name: str
    owner: Optional[FrequencyCounterOwner]
    resetIntervalInMinutes: int

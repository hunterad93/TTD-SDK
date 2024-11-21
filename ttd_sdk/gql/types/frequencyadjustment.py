from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .frequencycounter import FrequencyCounter
    from .rangeofint32 import RangeOfInt32


@dataclass
class FrequencyAdjustment:
    """
    None
    """
    counter: Optional[FrequencyCounter]
    id: str
    timesShown: Optional[RangeOfInt32]

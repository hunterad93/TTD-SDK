from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .rangeofint32 import RangeOfInt32


@dataclass
class FrequencyLegacyAdjustment:
    """
    None
    """
    lookBackWindowInMinutes: int
    timesShown: Optional[RangeOfInt32]

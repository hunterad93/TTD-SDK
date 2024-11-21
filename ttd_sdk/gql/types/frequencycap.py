from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .frequencycapperiod import FrequencyCapPeriod


@dataclass
class FrequencyCap:
    """
    Frequency cap
    """
    impressions: int
    periods: int
    periodType: Optional[FrequencyCapPeriod]

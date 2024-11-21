from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .frequencycounter import FrequencyCounter


@dataclass
class Increment:
    """
    None
    """
    creationDateUtc: Any
    frequencyCounter: Optional[FrequencyCounter]

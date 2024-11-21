from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .frequencycounterincrementorowner import FrequencyCounterIncrementorOwner


@dataclass
class FrequencyCounterIncrementor:
    """
    None
    """
    creationDate: Any
    id: str
    isDeleted: bool
    owner: Optional[FrequencyCounterIncrementorOwner]

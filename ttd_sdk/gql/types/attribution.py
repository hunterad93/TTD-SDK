from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .intervalgrain import IntervalGrain


@dataclass
class Attribution:
    """
    None
    """
    clickInterval: Optional[IntervalGrain]
    clickLookbackWindow: Any
    impressionInterval: Optional[IntervalGrain]
    impressionLookbackWindow: Any

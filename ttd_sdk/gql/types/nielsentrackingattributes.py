from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .enhancednielsenreportingoptions import EnhancedNielsenReportingOptions
    from .targetingendage import TargetingEndAge
    from .targetinggender import TargetingGender
    from .targetingstartage import TargetingStartAge


@dataclass
class NielsenTrackingAttributes:
    """
    None
    """
    countries: List[str]
    endAge: Optional[TargetingEndAge]
    enhancedNielsenReportingOptions: Optional[EnhancedNielsenReportingOptions]
    gender: Optional[TargetingGender]
    startAge: Optional[TargetingStartAge]


from enum import Enum

class BidListAdjustmentType(Enum):
    """
    None
    """
    EXCLUSION = "EXCLUSION"
    FRACTIONAL_EXCLUSION = "FRACTIONAL_EXCLUSION"
    INCLUSION = "INCLUSION"
    OPTIMIZED = "OPTIMIZED"
    VC_PROMOTION = "VC_PROMOTION"

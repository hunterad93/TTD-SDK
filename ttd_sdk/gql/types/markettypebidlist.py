
from enum import Enum

class MarketTypeBidList(Enum):
    """
    None
    """
    NON_PMP_FIXED = "NON_PMP_FIXED"
    OPEN_MARKET = "OPEN_MARKET"
    PMP_FIXED = "PMP_FIXED"
    PMP_NOT_SPECIFIED = "PMP_NOT_SPECIFIED"
    PMP_VARIABLE = "PMP_VARIABLE"
    UNKNOWN = "UNKNOWN"

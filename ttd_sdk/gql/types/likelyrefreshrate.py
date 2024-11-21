
from enum import Enum

class LikelyRefreshRate(Enum):
    """
    None
    """
    BETWEEN15_AND30 = "BETWEEN15_AND30"
    BETWEEN30_AND60 = "BETWEEN30_AND60"
    OVER60 = "OVER60"
    UNDER15 = "UNDER15"
    UNKNOWN = "UNKNOWN"

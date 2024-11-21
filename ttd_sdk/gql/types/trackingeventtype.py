
from enum import Enum

class TrackingEventType(Enum):
    """
    None
    """
    CLICK = "CLICK"
    COMPLETE = "COMPLETE"
    FIRST_QUARTILE = "FIRST_QUARTILE"
    IMPRESSION = "IMPRESSION"
    MIDPOINT = "MIDPOINT"
    START = "START"
    THIRD_QUARTILE = "THIRD_QUARTILE"

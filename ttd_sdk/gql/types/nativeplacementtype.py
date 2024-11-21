
from enum import Enum

class NativePlacementType(Enum):
    """
    None
    """
    IN_FEED = "IN_FEED"
    INSIDE_CONTENT = "INSIDE_CONTENT"
    OUTSIDE_CONTENT = "OUTSIDE_CONTENT"
    RECOMMENDATION_WIDGET = "RECOMMENDATION_WIDGET"
    UNKNOWN = "UNKNOWN"

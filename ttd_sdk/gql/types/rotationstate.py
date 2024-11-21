
from enum import Enum

class RotationState(Enum):
    """
    None
    """
    NOT_ROTATING = "NOT_ROTATING"
    POTENTIALLY_ROTATING = "POTENTIALLY_ROTATING"
    ROTATING = "ROTATING"

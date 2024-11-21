
from enum import Enum

class DaastErrorCode(Enum):
    """
    None
    """
    DAAST_VALIDATION_ERROR = "DAAST_VALIDATION_ERROR"
    DURATION_OUT_OF_RANGE = "DURATION_OUT_OF_RANGE"
    NO_DURATION = "NO_DURATION"
    NO_MEDIA_FILES = "NO_MEDIA_FILES"

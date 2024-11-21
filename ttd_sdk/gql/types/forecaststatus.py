
from enum import Enum

class ForecastStatus(Enum):
    """
    None
    """
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    TO_BE_SUBMITTED = "TO_BE_SUBMITTED"

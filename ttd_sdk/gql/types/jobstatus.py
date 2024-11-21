
from enum import Enum

class JobStatus(Enum):
    """
    None
    """
    COMPLETE = "COMPLETE"
    ERROR = "ERROR"
    IN_PROGRESS = "IN_PROGRESS"
    VALIDATION_FAILURE = "VALIDATION_FAILURE"
    FAILED = "FAILED"
    SCHEDULED = "SCHEDULED"


from enum import Enum

class CloneJobStatus(Enum):
    """
    None
    """
    BUILDING = "BUILDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IGNORED = "IGNORED"
    PROCESSING = "PROCESSING"
    QUEUED = "QUEUED"

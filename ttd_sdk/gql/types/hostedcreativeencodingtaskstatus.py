
from enum import Enum

class HostedCreativeEncodingTaskStatus(Enum):
    """
    None
    """
    COMPLETE = "COMPLETE"
    DUPLICATE = "DUPLICATE"
    ENCODING = "ENCODING"
    ERROR = "ERROR"
    PENDING = "PENDING"
    READY = "READY"
    SCHEDULED = "SCHEDULED"

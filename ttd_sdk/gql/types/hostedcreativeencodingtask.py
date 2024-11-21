from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .hostedcreativeencodingtaskstatus import HostedCreativeEncodingTaskStatus


@dataclass
class HostedCreativeEncodingTask:
    """
    None
    """
    encodingError: str
    encodingTaskStatus: Optional[HostedCreativeEncodingTaskStatus]
    sourceFile: str
    status: Optional[HostedCreativeEncodingTaskStatus]

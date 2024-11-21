from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .jobstatus import JobStatus


@dataclass
class ScheduledReportJobStatusResponse:
    """
    None
    """
    status: Optional[JobStatus]
    url: str

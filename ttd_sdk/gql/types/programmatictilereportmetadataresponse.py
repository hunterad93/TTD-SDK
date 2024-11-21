from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .reporttype import ReportType
    from .scheduletype import ScheduleType


@dataclass
class ProgrammaticTileReportMetadataResponse:
    """
    None
    """
    available: bool
    schedule: Optional[ScheduleType]
    type: Optional[ReportType]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .reportdelivery import ReportDelivery


@dataclass
class ProgrammaticReportMetadata:
    """
    None
    """
    available: bool
    name: str
    schedule: Optional[ReportDelivery]

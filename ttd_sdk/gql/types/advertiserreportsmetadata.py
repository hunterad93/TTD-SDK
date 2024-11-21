from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .programmaticreportmetadata import ProgrammaticReportMetadata


@dataclass
class AdvertiserReportsMetadata:
    """
    None
    """
    advertiserTile: List[Optional[ProgrammaticReportMetadata]]
    audienceTile: List[Optional[ProgrammaticReportMetadata]]

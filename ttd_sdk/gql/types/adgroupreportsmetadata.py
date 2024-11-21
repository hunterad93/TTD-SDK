from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .programmaticreportmetadata import ProgrammaticReportMetadata


@dataclass
class AdGroupReportsMetadata:
    """
    None
    """
    adFormatTile: List[Optional[ProgrammaticReportMetadata]]
    adGroupTile: List[Optional[ProgrammaticReportMetadata]]
    advertiserTile: List[Optional[ProgrammaticReportMetadata]]
    audienceTile: List[Optional[ProgrammaticReportMetadata]]
    campaignTile: List[Optional[ProgrammaticReportMetadata]]
    contextualTile: List[Optional[ProgrammaticReportMetadata]]
    creativeSelectionTile: List[Optional[ProgrammaticReportMetadata]]
    deviceDetailsTile: List[Optional[ProgrammaticReportMetadata]]
    geographyTile: List[Optional[ProgrammaticReportMetadata]]
    inventoryControlsTile: List[Optional[ProgrammaticReportMetadata]]
    inventorySelectionTile: List[Optional[ProgrammaticReportMetadata]]
    languageTile: List[Optional[ProgrammaticReportMetadata]]
    reachAndFrequencyTile: List[Optional[ProgrammaticReportMetadata]]
    recencyTile: List[Optional[ProgrammaticReportMetadata]]
    timeDayAndWeekTile: List[Optional[ProgrammaticReportMetadata]]
    viewabilityTile: List[Optional[ProgrammaticReportMetadata]]
    weatherTile: List[Optional[ProgrammaticReportMetadata]]

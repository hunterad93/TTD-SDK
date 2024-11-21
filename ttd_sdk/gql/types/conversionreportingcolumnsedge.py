from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignconversionreportingcolumn import CampaignConversionReportingColumn


@dataclass
class ConversionReportingColumnsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[CampaignConversionReportingColumn]

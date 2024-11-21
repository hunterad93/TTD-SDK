from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignconversionreportingcolumn import CampaignConversionReportingColumn
    from .conversionreportingcolumnsedge import ConversionReportingColumnsEdge
    from .pageinfo import PageInfo


@dataclass
class ConversionReportingColumnsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ConversionReportingColumnsEdge]]
    nodes: List[Optional[CampaignConversionReportingColumn]]
    pageInfo: Optional[PageInfo]
    totalCount: int

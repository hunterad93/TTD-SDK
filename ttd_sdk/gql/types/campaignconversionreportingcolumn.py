from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ccrcproductlistinfo import CcrcProductListInfo
    from .crossdeviceattribution import CrossDeviceAttribution
    from .customcpaconfig import CustomCPAConfig
    from .customroasconfig import CustomROASConfig
    from .trackingtag import TrackingTag


@dataclass
class CampaignConversionReportingColumn:
    """
    None
    """
    crossDeviceAttribution: Optional[CrossDeviceAttribution]
    customCPAConfig: Optional[CustomCPAConfig]
    customROASConfig: Optional[CustomROASConfig]
    id: str
    productListInfo: Optional[CcrcProductListInfo]
    reportingColumnId: int
    trackingTag: Optional[TrackingTag]

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .productlistreportingtype import ProductListReportingType


@dataclass
class CcrcProductListInfo:
    """
    None
    """
    orderNumber: int
    type: Optional[ProductListReportingType]

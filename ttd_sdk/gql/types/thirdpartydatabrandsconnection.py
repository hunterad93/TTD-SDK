from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .thirdpartydatabrand import ThirdPartyDataBrand
    from .thirdpartydatabrandsedge import ThirdPartyDataBrandsEdge


@dataclass
class ThirdPartyDataBrandsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ThirdPartyDataBrandsEdge]]
    nodes: List[Optional[ThirdPartyDataBrand]]
    pageInfo: Optional[PageInfo]
    totalCount: int

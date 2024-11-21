from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .thirdpartydata import ThirdPartyData
    from .thirdpartydataedge import ThirdPartyDataEdge


@dataclass
class ThirdPartyDataConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ThirdPartyDataEdge]]
    nodes: List[Optional[ThirdPartyData]]
    pageInfo: Optional[PageInfo]
    totalCount: int

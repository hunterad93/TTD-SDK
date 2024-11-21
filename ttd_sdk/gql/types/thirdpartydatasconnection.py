from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .thirdpartydata import ThirdPartyData
    from .thirdpartydatasedge import ThirdPartyDatasEdge


@dataclass
class ThirdPartyDatasConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ThirdPartyDatasEdge]]
    nodes: List[Optional[ThirdPartyData]]
    pageInfo: Optional[PageInfo]
    totalCount: int

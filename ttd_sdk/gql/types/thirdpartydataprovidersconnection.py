from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .thirdpartydataprovider import ThirdPartyDataProvider
    from .thirdpartydataprovidersedge import ThirdPartyDataProvidersEdge


@dataclass
class ThirdPartyDataProvidersConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[ThirdPartyDataProvidersEdge]]
    nodes: List[Optional[ThirdPartyDataProvider]]
    pageInfo: Optional[PageInfo]
    totalCount: int

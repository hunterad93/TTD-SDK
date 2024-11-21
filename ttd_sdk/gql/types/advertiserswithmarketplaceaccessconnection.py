from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser
    from .advertiserswithmarketplaceaccessedge import AdvertisersWithMarketplaceAccessEdge
    from .pageinfo import PageInfo


@dataclass
class AdvertisersWithMarketplaceAccessConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AdvertisersWithMarketplaceAccessEdge]]
    nodes: List[Optional[Advertiser]]
    pageInfo: Optional[PageInfo]
    totalCount: int

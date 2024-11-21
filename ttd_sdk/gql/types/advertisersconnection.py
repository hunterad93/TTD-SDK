from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser
    from .advertisersedge import AdvertisersEdge
    from .pageinfo import PageInfo


@dataclass
class AdvertisersConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[AdvertisersEdge]]
    nodes: List[Optional[Advertiser]]
    pageInfo: Optional[PageInfo]
    totalCount: int

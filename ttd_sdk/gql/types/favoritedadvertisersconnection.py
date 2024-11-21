from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser
    from .favoritedadvertisersedge import FavoritedAdvertisersEdge
    from .pageinfo import PageInfo


@dataclass
class FavoritedAdvertisersConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[FavoritedAdvertisersEdge]]
    nodes: List[Optional[Advertiser]]
    pageInfo: Optional[PageInfo]
    totalCount: int

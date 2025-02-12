from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser


@dataclass
class AdvertisersEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[Advertiser]

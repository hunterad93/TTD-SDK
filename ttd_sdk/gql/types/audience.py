from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser


@dataclass
class Audience:
    """
    None
    """
    advertiser: Optional[Advertiser]
    createdAt: Any
    id: str
    name: str

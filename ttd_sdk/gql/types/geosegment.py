from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser
    from .partner import Partner


@dataclass
class GeoSegment:
    """
    None
    """
    advertiser: Optional[Advertiser]
    description: str
    id: str
    isDeprecated: bool
    isStandard: bool
    name: str
    partner: Optional[Partner]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .partner import Partner


@dataclass
class PartnersWithMarketplaceAccessEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[Partner]

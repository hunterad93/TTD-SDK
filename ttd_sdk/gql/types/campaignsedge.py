from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaign import Campaign


@dataclass
class CampaignsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[Campaign]

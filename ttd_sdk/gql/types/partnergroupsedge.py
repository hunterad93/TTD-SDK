from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .partnergroup import PartnerGroup


@dataclass
class PartnerGroupsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[PartnerGroup]

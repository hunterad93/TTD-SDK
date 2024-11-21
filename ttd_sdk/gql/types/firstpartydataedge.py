from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .firstpartydata import FirstPartyData


@dataclass
class FirstPartyDataEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[FirstPartyData]

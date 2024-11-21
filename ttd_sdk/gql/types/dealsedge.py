from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .privatecontract import PrivateContract


@dataclass
class DealsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[PrivateContract]

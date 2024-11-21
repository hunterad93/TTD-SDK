from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .associatedbidlist import AssociatedBidList


@dataclass
class AssociatedBidListsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[AssociatedBidList]

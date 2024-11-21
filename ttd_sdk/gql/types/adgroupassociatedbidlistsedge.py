from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupassociatedbidlist import AdGroupAssociatedBidList


@dataclass
class AdGroupAssociatedBidListsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[AdGroupAssociatedBidList]

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .firstpartydata import FirstPartyData
    from .firstpartydataedge import FirstPartyDataEdge
    from .pageinfo import PageInfo


@dataclass
class FirstPartyDataConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[FirstPartyDataEdge]]
    nodes: List[Optional[FirstPartyData]]
    pageInfo: Optional[PageInfo]
    totalCount: int

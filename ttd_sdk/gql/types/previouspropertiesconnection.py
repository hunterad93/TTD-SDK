from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .previouspropertiesedge import PreviousPropertiesEdge
    from .publisherproperty import PublisherProperty


@dataclass
class PreviousPropertiesConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PreviousPropertiesEdge]]
    nodes: List[Optional[PublisherProperty]]
    pageInfo: Optional[PageInfo]
    totalCount: int

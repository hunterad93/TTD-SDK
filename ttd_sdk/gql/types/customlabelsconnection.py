from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .customlabel import CustomLabel
    from .customlabelsedge import CustomLabelsEdge
    from .pageinfo import PageInfo


@dataclass
class CustomLabelsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[CustomLabelsEdge]]
    nodes: List[Optional[CustomLabel]]
    pageInfo: Optional[PageInfo]
    totalCount: int

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creativeissue import CreativeIssue


@dataclass
class CreativeIssuesEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[CreativeIssue]

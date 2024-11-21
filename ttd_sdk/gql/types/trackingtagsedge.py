from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .trackingtag import TrackingTag


@dataclass
class TrackingTagsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[TrackingTag]

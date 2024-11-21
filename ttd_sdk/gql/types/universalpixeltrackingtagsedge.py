from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .universalpixeltrackingtag import UniversalPixelTrackingTag


@dataclass
class UniversalPixelTrackingTagsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[UniversalPixelTrackingTag]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .universalpixeltrackingtagsconnection import UniversalPixelTrackingTagsConnection


@dataclass
class UniversalPixel:
    """
    None
    """
    id: str
    name: str
    universalPixelTrackingTags: Optional[UniversalPixelTrackingTagsConnection]

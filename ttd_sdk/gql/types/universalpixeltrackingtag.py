from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .trackingtag import TrackingTag


@dataclass
class UniversalPixelTrackingTag:
    """
    None
    """
    trackingTag: Optional[TrackingTag]
    urlPattern: str

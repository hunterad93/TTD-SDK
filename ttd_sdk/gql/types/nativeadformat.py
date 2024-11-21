from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .mediatype import MediaType


@dataclass
class NativeAdFormat:
    """
    None
    """
    heightInPixels: int
    iabName: str
    id: str
    mediaType: Optional[MediaType]
    userFriendlyLabel: str
    widthInPixels: int

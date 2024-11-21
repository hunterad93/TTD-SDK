from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .resolution import Resolution


@dataclass
class DetectedRendition:
    """
    None
    """
    bitrate: int
    fileSize: int
    fileSizeInBytes: int
    fileType: str
    resolution: Optional[Resolution]

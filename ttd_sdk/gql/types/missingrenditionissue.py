from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bitrate import Bitrate
    from .curatedpublisher import CuratedPublisher
    from .detectedrendition import DetectedRendition
    from .encodingissuecode import EncodingIssueCode
    from .encodingresolution import EncodingResolution


@dataclass
class MissingRenditionIssue:
    """
    None
    """
    bitrate: Optional[Bitrate]
    curatedPublisher: Optional[CuratedPublisher]
    detectedRendition: Optional[DetectedRendition]
    issues: List[Optional[EncodingIssueCode]]
    maxFileSize: int
    maxFileSizeInBytes: int
    missingFileTypes: List[str]
    resolution: Optional[EncodingResolution]

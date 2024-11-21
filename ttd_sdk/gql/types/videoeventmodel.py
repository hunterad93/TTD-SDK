from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .videoeventtype import VideoEventType


@dataclass
class VideoEventModel:
    """
    None
    """
    type: Optional[VideoEventType]
    url: str

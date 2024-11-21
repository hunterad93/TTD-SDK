from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .curatedpublisher import CuratedPublisher


@dataclass
class MissingFileTypeIssue:
    """
    None
    """
    curatedPublisher: Optional[CuratedPublisher]
    missingFileTypes: List[str]
    missingRecommendedFileTypes: List[str]

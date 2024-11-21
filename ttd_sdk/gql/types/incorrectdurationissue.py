from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .curatedpublisher import CuratedPublisher


@dataclass
class IncorrectDurationIssue:
    """
    None
    """
    curatedPublisher: Optional[CuratedPublisher]
    detectedDurationInSeconds: int
    maxDurationInSeconds: int
    minDurationInSeconds: int

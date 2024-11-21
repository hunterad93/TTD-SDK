from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .curatedpublisher import CuratedPublisher


@dataclass
class IncorrectVastVersionIssue:
    """
    None
    """
    curatedPublisher: Optional[CuratedPublisher]
    detectedVastVersion: int
    maxVersion: int
    minVersion: int

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup


@dataclass
class AdGroupCloneFailurePairing:
    """
    A pairing of source AdGroups with their cloning failure reason.
    """
    adGroup: Optional[AdGroup]
    failureMessage: str

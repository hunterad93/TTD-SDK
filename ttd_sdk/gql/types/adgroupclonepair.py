from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup


@dataclass
class AdGroupClonePair:
    """
    A pairing of original AdGroup ID to its cloned counterpart.
    """
    clonedAdGroup: Optional[AdGroup]
    originalAdGroup: Optional[AdGroup]

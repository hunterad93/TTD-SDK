from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creative import Creative


@dataclass
class AdGroupCreativesEdge:
    """
    An edge in a connection.
    """
    cursor: str
    manualWeight: Any
    node: Optional[Creative]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creative import Creative


@dataclass
class CompanionCreativesEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[Creative]
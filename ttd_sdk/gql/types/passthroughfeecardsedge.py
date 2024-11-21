from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .passthroughfeecard import PassThroughFeeCard


@dataclass
class PassThroughFeeCardsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[PassThroughFeeCard]

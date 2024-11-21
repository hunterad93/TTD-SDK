from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .dataratecard import DataRateCard


@dataclass
class DataRateCardsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[DataRateCard]

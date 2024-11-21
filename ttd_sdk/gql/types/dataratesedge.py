from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .datarate import DataRate


@dataclass
class DataRatesEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[DataRate]

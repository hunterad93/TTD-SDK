from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .frequencycounter import FrequencyCounter


@dataclass
class ImpressionFrequencyCountersEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[FrequencyCounter]

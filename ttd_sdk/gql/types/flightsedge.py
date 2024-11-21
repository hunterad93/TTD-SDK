from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignflight import CampaignFlight


@dataclass
class FlightsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[CampaignFlight]

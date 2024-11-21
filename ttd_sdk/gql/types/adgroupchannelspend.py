from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .inventorychanneltype import InventoryChannelType


@dataclass
class AdGroupChannelSpend:
    """
    None
    """
    channel: Optional[InventoryChannelType]
    partnerCostInUSD: Any
    partnerCostPercentage: Any

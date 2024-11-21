from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .dealsconnection import DealsConnection
    from .recommendationowner import RecommendationOwner


@dataclass
class InventorySelectionDeals:
    """
    Recommendation of type 3 from Inventory Selection. Contains a list of deals recommended to be adopted
    """
    deals: Optional[DealsConnection]
    domain: str
    id: str
    owner: Optional[RecommendationOwner]
    updatedAt: Any
    version: int

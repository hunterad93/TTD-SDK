from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .propertiesconnection import PropertiesConnection
    from .recommendationowner import RecommendationOwner


@dataclass
class InventorySelectionProperties:
    """
    Recommendation of type 2 from Inventory Selection. Contains a list of properties recommended to be adopted
    """
    domain: str
    id: str
    owner: Optional[RecommendationOwner]
    properties: Optional[PropertiesConnection]
    updatedAt: Any
    version: int

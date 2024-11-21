from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .inventoryrecommendationdeal import InventoryRecommendationDeal
    from .publisher import Publisher
    from .publisherpropertymappingsconnection import PublisherPropertyMappingsConnection
    from .publisherpropertysearchterms import PublisherPropertySearchTerms
    from .spendconnection import SpendConnection


@dataclass
class PublisherProperty:
    """
    None
    """
    creationDate: Any
    description: str
    globalSortOrder: int
    id: str
    isCTV: bool
    isDisplay: bool
    isFeatured: bool
    isFilteredForBadQuality: bool
    isGlobal: bool
    isInApp: bool
    isVideo: bool
    isWeb: bool
    lastUpdateDate: Any
    lastUpdatedBy: str
    logo: str
    name: str
    ownerPublisher: Optional[Publisher]
    publisherPropertyMappings: Optional[PublisherPropertyMappingsConnection]
    publisherPropertyMappingsCount: int
    searchTerms: Optional[PublisherPropertySearchTerms]
    spend: Optional[SpendConnection]
    deals: List[Optional[InventoryRecommendationDeal]]

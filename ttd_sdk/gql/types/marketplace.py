from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiserswithmarketplaceaccessconnection import AdvertisersWithMarketplaceAccessConnection
    from .marketplaceowner import MarketplaceOwner
    from .partnerswithmarketplaceaccessconnection import PartnersWithMarketplaceAccessConnection
    from .passthroughfeecardsconnection import PassThroughFeeCardsConnection


@dataclass
class Marketplace:
    """
    Marketplace definition
    """
    advertisersWithMarketplaceAccess: Optional[AdvertisersWithMarketplaceAccessConnection]
    id: str
    name: str
    owner: Optional[MarketplaceOwner]
    partnersWithMarketplaceAccess: Optional[PartnersWithMarketplaceAccessConnection]
    passThroughFeeCards: Optional[PassThroughFeeCardsConnection]

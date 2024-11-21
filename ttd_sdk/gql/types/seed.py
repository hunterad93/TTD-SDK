from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser
    from .campaignsconnection import CampaignsConnection
    from .seedquality import SeedQuality
    from .seedtargetingdata import SeedTargetingData


@dataclass
class Seed:
    """
    None
    """
    activeIds: int
    advertiser: Optional[Advertiser]
    campaigns: Optional[CampaignsConnection]
    createdAt: Any
    id: str
    isDefault: bool
    lastUpdatedAt: Any
    name: str
    quality: Optional[SeedQuality]
    status: str
    targetingData: Optional[SeedTargetingData]
    uniqueHouseholds: int

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .country import Country
    from .dbopublisher import DboPublisher
    from .region import Region
    from .supplyvendor import SupplyVendor


@dataclass
class TMTAdPolicyBiddingLimitationsInfo:
    """
    None
    """
    blockedCountry: Optional[Country]
    blockedRegion: Optional[Region]
    blockedSupplyVendor: Optional[SupplyVendor]
    blockedSupplyVendorPublisher: Optional[DboPublisher]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .publisher import Publisher
    from .supplyvendor import SupplyVendor


@dataclass
class SupplyVendorPublisher:
    """
    None
    """
    supplyVendorId: int
    supplyVendorPublisherId: str
    publisher: Optional[Publisher]
    supplyVendor: Optional[SupplyVendor]

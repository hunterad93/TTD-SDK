from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .supplyvendorauditstatus import SupplyVendorAuditStatus
    from .supplyvendorpublisherauditstatus import SupplyVendorPublisherAuditStatus


@dataclass
class AuditStatuses:
    """
    None
    """
    supplyVendorAuditStatuses: List[Optional[SupplyVendorAuditStatus]]
    supplyVendorPublisherAuditStatuses: List[Optional[SupplyVendorPublisherAuditStatus]]

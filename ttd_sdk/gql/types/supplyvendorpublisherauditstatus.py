from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creativeauditstatus import CreativeAuditStatus
    from .supplyvendorpublisher import SupplyVendorPublisher


@dataclass
class SupplyVendorPublisherAuditStatus:
    """
    Audit status for Publishers inventory when bought via given supply vendor. Each publisher - supply vendor combination can have its own audit status.
    """
    auditFeedback: str
    auditStatus: str
    auditStatusEnum: Optional[CreativeAuditStatus]
    creativeApproverId: int
    supplyVendorPublisher: Optional[SupplyVendorPublisher]

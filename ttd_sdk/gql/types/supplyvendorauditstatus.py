from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creativeauditstatus import CreativeAuditStatus
    from .supplyvendor import SupplyVendor


@dataclass
class SupplyVendorAuditStatus:
    """
    Audit status for all inventory bought via this supply vendor.
    """
    auditFeedback: str
    auditStatus: str
    auditStatusEnum: Optional[CreativeAuditStatus]
    isOpenPath: bool
    submissionState: str
    submittedAt: Any
    supplyVendor: Optional[SupplyVendor]

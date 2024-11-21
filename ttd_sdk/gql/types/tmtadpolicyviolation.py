from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adpolicyviolationexemption import AdPolicyViolationExemption
    from .tmtadpolicybiddinglimitations import TMTAdPolicyBiddingLimitations
    from .tenant import Tenant


@dataclass
class TMTAdPolicyViolation:
    """
    None
    """
    biddingLimitations: Optional[TMTAdPolicyBiddingLimitations]
    exemptionDetails: Optional[AdPolicyViolationExemption]
    isBidBlocking: bool
    isWalmartPolicy: bool
    lastSeenAt: Any
    policyId: str
    policyName: str
    source: Optional[Tenant]

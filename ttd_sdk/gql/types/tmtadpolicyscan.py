from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tmtadpolicyviolation import TMTAdPolicyViolation


@dataclass
class TMTAdPolicyScan:
    """
    None
    """
    policyViolations: List[Optional[TMTAdPolicyViolation]]

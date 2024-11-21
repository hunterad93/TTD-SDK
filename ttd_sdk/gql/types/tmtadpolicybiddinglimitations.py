from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tmtadpolicybiddinglimitationsinfo import TMTAdPolicyBiddingLimitationsInfo


@dataclass
class TMTAdPolicyBiddingLimitations:
    """
    None
    """
    biddingLimitationsInfo: List[Optional[TMTAdPolicyBiddingLimitationsInfo]]
    isGloballyBidBlocking: bool

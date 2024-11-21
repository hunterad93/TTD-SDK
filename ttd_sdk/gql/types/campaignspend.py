from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .riskindicatorlevel import RiskIndicatorLevel


@dataclass
class CampaignSpend:
    """
    None
    """
    current: Any
    riskLevel: Optional[RiskIndicatorLevel]

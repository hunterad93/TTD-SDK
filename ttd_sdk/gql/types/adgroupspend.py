from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .riskindicatorlevel import RiskIndicatorLevel


@dataclass
class AdGroupSpend:
    """
    None
    """
    riskLevel: Optional[RiskIndicatorLevel]
    spend: Any

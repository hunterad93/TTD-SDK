from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .feetype import FeeType


@dataclass
class ExpandableFee:
    """
    None
    """
    currencyCodeId: str
    expandableFeeInCurrencyOrPercentage: Any
    expandableFeeType: Optional[FeeType]

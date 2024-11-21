from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .currencycode import CurrencyCode


@dataclass
class MoneyModel:
    """
    None
    """
    amount: Any
    currencyCode: Optional[CurrencyCode]

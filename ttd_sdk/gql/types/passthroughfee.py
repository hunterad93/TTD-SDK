from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .passthroughfeetype import PassThroughFeeType


@dataclass
class PassThroughFee:
    """
    None
    """
    amount: Any
    currencyCodeId: str
    description: str
    id: int
    type: Optional[PassThroughFeeType]

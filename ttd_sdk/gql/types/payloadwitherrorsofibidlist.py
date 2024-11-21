from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ibidlist import IBidList
    from .usererror import UserError


@dataclass
class PayloadWithErrorsOfIBidList:
    """
    Represents the executed state of a mutation, including all data and userErrors produced as a result of the operation.
    """
    data: Optional[IBidList]
    userErrors: List[Optional[UserError]]

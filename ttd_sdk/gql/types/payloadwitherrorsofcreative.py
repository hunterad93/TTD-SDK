from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creative import Creative
    from .usererror import UserError


@dataclass
class PayloadWithErrorsOfCreative:
    """
    Represents the executed state of a mutation, including all data and userErrors produced as a result of the operation.
    """
    data: Optional[Creative]
    userErrors: List[Optional[UserError]]

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaign import Campaign
    from .usererror import UserError


@dataclass
class PayloadWithErrorsOfCampaign:
    """
    Represents the executed state of a mutation, including all data and userErrors produced as a result of the operation.
    """
    data: Optional[Campaign]
    userErrors: List[Optional[UserError]]

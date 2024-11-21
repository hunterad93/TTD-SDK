from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignflightdeletereturn import CampaignFlightDeleteReturn
    from .usererror import UserError


@dataclass
class PayloadWithErrorsOfCampaignFlightDeleteReturn:
    """
    Represents the executed state of a mutation, including all data and userErrors produced as a result of the operation.
    """
    data: Optional[CampaignFlightDeleteReturn]
    userErrors: List[Optional[UserError]]

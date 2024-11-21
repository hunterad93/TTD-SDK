from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaigncloneprogress import CampaignCloneProgress
    from .usererror import UserError


@dataclass
class PayloadWithErrorsOfListOfCampaignCloneProgress:
    """
    Represents the executed state of a mutation, including all data and userErrors produced as a result of the operation.
    """
    data: List[Optional[CampaignCloneProgress]]
    userErrors: List[Optional[UserError]]

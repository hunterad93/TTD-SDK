from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignversionupgradereturn import CampaignVersionUpgradeReturn
    from .usererror import UserError


@dataclass
class PayloadWithErrorsOfListOfCampaignVersionUpgradeReturn:
    """
    Represents the executed state of a mutation, including all data and userErrors produced as a result of the operation.
    """
    data: List[Optional[CampaignVersionUpgradeReturn]]
    userErrors: List[Optional[UserError]]

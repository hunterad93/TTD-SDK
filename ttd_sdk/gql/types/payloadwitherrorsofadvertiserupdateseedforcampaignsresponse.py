from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiserupdateseedforcampaignsresponse import AdvertiserUpdateSeedForCampaignsResponse
    from .usererror import UserError


@dataclass
class PayloadWithErrorsOfAdvertiserUpdateSeedForCampaignsResponse:
    """
    Represents the executed state of a mutation, including all data and userErrors produced as a result of the operation.
    """
    data: Optional[AdvertiserUpdateSeedForCampaignsResponse]
    userErrors: List[Optional[UserError]]

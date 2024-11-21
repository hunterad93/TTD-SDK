from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaign import Campaign


@dataclass
class CampaignBudgetSettingsUpdateReturn:
    """
    None
    """
    campaign: Optional[Campaign]
    wasBudgetUpdated: bool

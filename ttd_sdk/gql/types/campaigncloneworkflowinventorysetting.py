from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaigncloneworkflowinventorytype import CampaignCloneWorkflowInventoryType


@dataclass
class CampaignCloneWorkflowInventorySetting:
    """
    Inventory settings for an ad group on the context of Campaign Clone.
    """
    inventoryType: Optional[CampaignCloneWorkflowInventoryType]
    marketplaceName: str

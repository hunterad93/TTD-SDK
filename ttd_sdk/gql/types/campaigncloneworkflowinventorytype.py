
from enum import Enum

class CampaignCloneWorkflowInventoryType(Enum):
    """
    Inventory type for ad groups in the context of Campaign Cloning.
    """
    BLUE_LIST = "BLUE_LIST"
    OPEN_MARKET = "OPEN_MARKET"
    PRIVATE_MARKET_ONLY = "PRIVATE_MARKET_ONLY"
    SP500_PLUS = "SP500_PLUS"

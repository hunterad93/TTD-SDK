from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaigncloneinventoryrecommendationadgroup import CampaignCloneInventoryRecommendationAdGroup
    from .marketplace import Marketplace
    from .workflowrecommendationtype import WorkflowRecommendationType


@dataclass
class CampaignCloneInventoryRecommendation:
    """
    None
    """
    adGroupRecommendations: List[Optional[CampaignCloneInventoryRecommendationAdGroup]]
    isDefaultMarketplaceRecommended: bool
    recommendationType: Optional[WorkflowRecommendationType]
    recommendedMarketplace: Optional[Marketplace]

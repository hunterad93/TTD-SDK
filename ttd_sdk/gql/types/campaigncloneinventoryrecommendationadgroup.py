from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup
    from .baserecommendation import BaseRecommendation
    from .campaigncloneinventoryrecommendationtype import CampaignCloneInventoryRecommendationType
    from .campaigncloneworkflowinventorysetting import CampaignCloneWorkflowInventorySetting
    from .previouspropertiesconnection import PreviousPropertiesConnection
    from .recommendedpropertiesconnection import RecommendedPropertiesConnection


@dataclass
class CampaignCloneInventoryRecommendationAdGroup:
    """
    Campaign cloning inventory recommendations for an ad group.
    """
    adGroup: Optional[AdGroup]
    campaignCloneInventoryRecommendationType: Optional[CampaignCloneInventoryRecommendationType]
    originalInventory: Optional[CampaignCloneWorkflowInventorySetting]
    previousProperties: Optional[PreviousPropertiesConnection]
    recommendation: Optional[BaseRecommendation]
    recommendedProperties: Optional[RecommendedPropertiesConnection]
    updatedAt: Any

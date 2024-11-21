from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup
    from .campaignclonerecommendationforecast import CampaignCloneRecommendationForecast


@dataclass
class CampaignCloneInventoryRecommendationAdGroupsLevelForecastResult:
    """
    Forecasts at Ad Group level for Campaign Cloning.
    """
    adGroup: Optional[AdGroup]
    originalForecast: Optional[CampaignCloneRecommendationForecast]
    recommendationsForecast: Optional[CampaignCloneRecommendationForecast]

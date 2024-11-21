from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaigncloneinventoryrecommendationadgroupslevelforecastresult import CampaignCloneInventoryRecommendationAdGroupsLevelForecastResult
    from .campaignclonerecommendationforecast import CampaignCloneRecommendationForecast


@dataclass
class CampaignCloneCampaignLevelForecastResult:
    """
    Forecasts at Campaign level and Ad Group level for Campaign Cloning.
    """
    adGroupLevelForecasts: List[Optional[CampaignCloneInventoryRecommendationAdGroupsLevelForecastResult]]
    originalForecast: Optional[CampaignCloneRecommendationForecast]
    recommendationsForecast: Optional[CampaignCloneRecommendationForecast]

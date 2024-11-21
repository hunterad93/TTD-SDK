from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignclonerecommendationsbreakdownforecastdetails import CampaignCloneRecommendationsBreakdownForecastDetails
    from .publisherproperty import PublisherProperty


@dataclass
class CampaignCloneInventoryRecommendationPropertyLevelForecastResult:
    """
    Forecasts at publisher property level for Campaign Cloning.
    """
    originalForecast: Optional[CampaignCloneRecommendationsBreakdownForecastDetails]
    publisherProperty: Optional[PublisherProperty]
    recommendationsForecast: Optional[CampaignCloneRecommendationsBreakdownForecastDetails]

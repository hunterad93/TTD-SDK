from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .omnichannelforecastrecommendationbasis import OmnichannelForecastRecommendationBasis
    from .omnichannelforecastrecommendationsourcetype import OmnichannelForecastRecommendationSourceType
    from .recommendedforecastsettings import RecommendedForecastSettings


@dataclass
class OmnichannelForecastRecommendation:
    """
    An omnichannel forecast recommendation.
    """
    recommendationBasis: Optional[OmnichannelForecastRecommendationBasis]
    recommendationSource: Optional[OmnichannelForecastRecommendationSourceType]
    recommendedSettings: Optional[RecommendedForecastSettings]

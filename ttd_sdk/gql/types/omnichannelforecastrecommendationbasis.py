from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .omnichannelforecastrecommendationbasistype import OmnichannelForecastRecommendationBasisType


@dataclass
class OmnichannelForecastRecommendationBasis:
    """
    Basis for an omnichannel forecast recommendation.
    """
    percentageChange: Any
    type: Optional[OmnichannelForecastRecommendationBasisType]

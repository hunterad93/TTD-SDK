from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaignchannel import CampaignChannel


@dataclass
class OmnichannelGroupConversionPath:
    """
    Omnichannel group PTC report row.
    """
    advertiserCostInAdvertiserCurrency: Any
    avgSecondsFirstImpressionToConversion: int
    conversionCount: int
    conversionRate: float
    impressionCount: int
    pathChannels: List[Optional[CampaignChannel]]
    reachBasedConversionRate: float
    uniqueConvertedReachCount: int
    uniqueReachCount: int

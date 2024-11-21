from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup
    from .adgroupflightforecast import AdGroupFlightForecast
    from .campaign import Campaign
    from .campaignflight import CampaignFlight


@dataclass
class AdGroupFlight:
    """
    None
    """
    adGroup: Optional[AdGroup]
    adGroupId: str
    budgetInAdvertiserCurrency: Any
    budgetInImpressions: int
    campaign: Optional[Campaign]
    campaignFlight: Optional[CampaignFlight]
    campaignFlightId: int
    dailyTargetInAdvertiserCurrency: Any
    dailyTargetInImpressions: int
    forecast: Optional[AdGroupFlightForecast]
    minimumSpendInAdvertiserCurrency: Any

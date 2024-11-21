from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupflightsconnection import AdGroupFlightsConnection
    from .campaign import Campaign
    from .campaignbudgetallocationmode import CampaignBudgetAllocationMode
    from .campaignflightforecast import CampaignFlightForecast
    from .campaignflightreporting import CampaignFlightReporting


@dataclass
class CampaignFlight:
    """
    None
    """
    adGroupFlights: Optional[AdGroupFlightsConnection]
    budgetAllocationMode: Optional[CampaignBudgetAllocationMode]
    budgetInAdvertiserCurrency: Any
    budgetInImpressions: int
    campaign: Optional[Campaign]
    dailyTargetInAdvertiserCurrency: Any
    dailyTargetInImpressions: int
    daysRemaining: float
    endDateExclusiveUTC: Any
    forecast: Optional[CampaignFlightForecast]
    id: str
    isActiveForAtLeastADay: bool
    isCurrent: bool
    isDeleted: bool
    startDateInclusiveUTC: Any
    reporting: Optional[CampaignFlightReporting]

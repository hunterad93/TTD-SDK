from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupspendsettingsmigrationdata import AdGroupSpendSettingsMigrationData
    from .campaignflightmigrationdata import CampaignFlightMigrationData
    from .campaignpacingmode import CampaignPacingMode


@dataclass
class CampaignBudgetMigrationData:
    """
    None
    """
    adGroupSpendSettings: List[Optional[AdGroupSpendSettingsMigrationData]]
    autoPrioritizationEnabled: bool
    campaignFlights: List[Optional[CampaignFlightMigrationData]]
    minimumAdGroupSpendInAdvertiserCurrency: Any
    pacingMode: Optional[CampaignPacingMode]

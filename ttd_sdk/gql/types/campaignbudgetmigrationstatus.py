from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaign import Campaign
    from .campaignbudgetmigrationdata import CampaignBudgetMigrationData
    from .campaignbudgetingversion import CampaignBudgetingVersion


@dataclass
class CampaignBudgetMigrationStatus:
    """
    None
    """
    campaign: Optional[Campaign]
    currentBudgetingVersion: Optional[CampaignBudgetingVersion]
    incompatibleFields: List[str]
    isCompatible: bool
    migrationData: Optional[CampaignBudgetMigrationData]

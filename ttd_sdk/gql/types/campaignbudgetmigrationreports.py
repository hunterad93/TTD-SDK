from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaign import Campaign
    from .campaignbudgetallocationmode import CampaignBudgetAllocationMode
    from .campaignbudgetingversion import CampaignBudgetingVersion
    from .campaignpacingmode import CampaignPacingMode


@dataclass
class CampaignBudgetMigrationReports:
    """
    None
    """
    allocationMode: Optional[CampaignBudgetAllocationMode]
    budgetingVersion: Optional[CampaignBudgetingVersion]
    campaign: Optional[Campaign]
    hasImpressions: bool
    hasLiveEvents: bool
    isMixedPacing: bool
    pacingMode: Optional[CampaignPacingMode]
    unifiedPacingMode: Optional[CampaignPacingMode]

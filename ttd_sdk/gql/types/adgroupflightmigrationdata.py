from dataclasses import dataclass

@dataclass
class AdGroupFlightMigrationData:
    """
    None
    """
    adGroupId: str
    adGroupName: str
    budgetInAdvertiserCurrency: Any
    budgetInImpressions: int
    campaignFlightId: int
    dailyTargetInAdvertiserCurrency: Any
    dailyTargetInImpressions: int
    minimumSpendInAdvertiserCurrency: Any

from dataclasses import dataclass

@dataclass
class ForecastingCurveDataPoint:
    """
    None
    """
    averageCpm: float
    averageFrequency: Any
    budget: Any
    decisionPower: int
    householdReach: int
    impressions: int
    personsReach: int
    relevance: float

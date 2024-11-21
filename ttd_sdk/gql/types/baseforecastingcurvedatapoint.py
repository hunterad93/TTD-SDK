from dataclasses import dataclass

@dataclass
class BaseForecastingCurveDataPoint:
    """
    None
    """
    averageFrequency: Any
    decisionPower: int
    householdReach: int
    impressions: int
    personsReach: int
    relevance: float

from dataclasses import dataclass

@dataclass
class AdGroupExpressiveness:
    """
    AdGroup expressiveness.
    """
    bidFactors: int
    dimensions: int
    score: float

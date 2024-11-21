from dataclasses import dataclass

@dataclass
class RecommendedProperty:
    """
    Represents a property recommended to a certain Adgroup or Campaign
    """
    availsCount: int
    id: str

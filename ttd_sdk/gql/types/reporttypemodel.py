from dataclasses import dataclass

@dataclass
class ReportTypeModel:
    """
    None
    """
    deprecationDate: Any
    hasConversions: bool
    hasGrains: bool
    hasMeasures: bool
    id: str
    isFixedGrainReport: bool
    isOverlapReport: bool
    name: str
    queryableDataAgeInDays: int
    queryableDataEarliestDate: Any
    requiredTimeZone: str
    requiresDateFilter: bool
    requiresPartnerFilter: bool

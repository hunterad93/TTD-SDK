from dataclasses import dataclass
from typing import List

@dataclass
class RetailerBrandRestrictions:
    """
    Restrictions of Retailer
    """
    restrictionDescriptionList: List[str]
    retailerLogoUrl: str
    retailerName: str

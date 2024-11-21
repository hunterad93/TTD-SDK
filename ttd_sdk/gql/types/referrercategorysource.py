from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .referrercategorysourcetactic import ReferrerCategorySourceTactic


@dataclass
class ReferrerCategorySource:
    """
    An enum that is mapped to code, whose purpose is to distinguish how categories in dbo.UniversalCategoryTaxonomy table should be used, and billed.
    """
    batchMarkerId: int
    enumName: str
    groupName: str
    id: str
    isCustom: bool
    isDeprecated: bool
    isPreBidContextual: bool
    markerId: int
    name: str
    shortName: str
    tactic: Optional[ReferrerCategorySourceTactic]

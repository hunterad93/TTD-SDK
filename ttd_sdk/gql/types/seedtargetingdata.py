from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contextualdata import ContextualData
    from .seedcountry import SeedCountry
    from .seedfirstpartydata import SeedFirstPartyData


@dataclass
class SeedTargetingData:
    """
    None
    """
    contextualInclusion: Optional[ContextualData]
    countryFilter: List[Optional[SeedCountry]]
    firstPartyInclusion: List[Optional[SeedFirstPartyData]]
    targetingDataId: str

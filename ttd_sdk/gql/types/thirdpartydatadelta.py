from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .thirdpartydata import ThirdPartyData


@dataclass
class ThirdPartyDataDelta:
    """
    The response for all changed Third Party Data for a given parent entity id (Advertiser) since the change tracking version.
    """
    currentMinimumTrackingVersion: int
    moreAvailable: bool
    nextChangeTrackingVersion: int
    thirdPartyData: List[Optional[ThirdPartyData]]

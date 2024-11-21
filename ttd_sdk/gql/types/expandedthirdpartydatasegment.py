from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .datarate import DataRate
    from .thirdpartydata import ThirdPartyData
    from .thirdpartydatabrand import ThirdPartyDataBrand
    from .thirdpartydataprovider import ThirdPartyDataProvider


@dataclass
class ExpandedThirdPartyDataSegment:
    """
    None
    """
    advertiserId: str
    buyable: bool
    dataRateLevelId: int
    fullPath: str
    inheritedFromThirdPartyDataRate: Optional[ThirdPartyData]
    inheritedThirdPartyDataId: int
    isCopiedDownRate: bool
    isInherited: bool
    partnerId: str
    thirdPartyData: Optional[ThirdPartyData]
    thirdPartyDataBrand: Optional[ThirdPartyDataBrand]
    thirdPartyDataProvider: Optional[ThirdPartyDataProvider]
    thirdPartyDataProviderElementId: str
    thirdPartyDataRate: Optional[DataRate]

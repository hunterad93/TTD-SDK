from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiser import Advertiser
    from .dataratesconnection import DataRatesConnection
    from .partner import Partner
    from .thirdpartydatabrand import ThirdPartyDataBrand


@dataclass
class DataRateCard:
    """
    None
    """
    advertiser: Optional[Advertiser]
    advertiserId: str
    brandFamilyCalculationEnabled: bool
    dataRates: Optional[DataRatesConnection]
    endDateExclusive: Any
    id: str
    isCurrent: bool
    isPartnerDirect: bool
    isPending: bool
    partner: Optional[Partner]
    partnerId: str
    startDateInclusive: Any
    thirdPartyDataBrand: Optional[ThirdPartyDataBrand]

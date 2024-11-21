from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .dataratecardsconnection import DataRateCardsConnection
    from .thirdpartydataprovider import ThirdPartyDataProvider


@dataclass
class ThirdPartyDataBrand:
    """
    None
    """
    allowApiAccessToProvider: bool
    brandCondensedLogoUrl: str
    brandDomainName: str
    brandFamilyName: str
    dataRateCards: Optional[DataRateCardsConnection]
    hasRestrictions: bool
    id: str
    isDeprecated: bool
    isPartnerDirectDefault: bool
    isPlannerModelingAllowed: bool
    isRetailProvider: bool
    logoUrl: str
    name: str
    thirdPartyDataProvider: Optional[ThirdPartyDataProvider]

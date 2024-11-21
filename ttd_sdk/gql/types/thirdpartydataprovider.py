from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .thirdpartydatabrandsconnection import ThirdPartyDataBrandsConnection
    from .thirdpartydataconnection import ThirdPartyDataConnection


@dataclass
class ThirdPartyDataProvider:
    """
    None
    """
    cloudServiceId: str
    cloudStorageProviderType: Any
    id: str
    importThirdPartyDataFromTargetingData: bool
    isAllowedInInsightsResults: bool
    isUserIdAlreadyHashed: bool
    name: str
    thirdPartyData: Optional[ThirdPartyDataConnection]
    thirdPartyDataBrands: Optional[ThirdPartyDataBrandsConnection]
    thirdPartyDataRootElementId: str
    thirdPartyDataUploadBucket: str
    thirdPartyDataUploadFolder: str

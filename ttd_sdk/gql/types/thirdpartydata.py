from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .activeuniques import ActiveUniques
    from .dataratesconnection import DataRatesConnection
    from .targetingdata import TargetingData
    from .targetingdatauniques import TargetingDataUniques
    from .targetingdatauniquesv2 import TargetingDataUniquesV2
    from .thirdpartydataprovider import ThirdPartyDataProvider


@dataclass
class ThirdPartyData:
    """
    None
    """
    activeUniques: Optional[ActiveUniques]
    allowCustomFullPath: bool
    audienceSize: int
    buyable: bool
    dataAllianceExcluded: bool
    dataRates: Optional[DataRatesConnection]
    defaultSortScore: float
    description: str
    fullPath: str
    generalPopulationOverlapLastUpdated: Any
    hierarchyString: str
    id: str
    importEnabled: bool
    isPlannerOnly: bool
    name: str
    parentId: str
    providerElementId: str
    providerId: str
    targetingData: Optional[TargetingData]
    targetingDataId: str
    targetingDataUniques: Optional[TargetingDataUniques]
    targetingDataUniquesV2: Optional[TargetingDataUniquesV2]
    thirdPartyDataProvider: Optional[ThirdPartyDataProvider]

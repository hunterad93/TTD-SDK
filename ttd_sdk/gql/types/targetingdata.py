from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .dataeventtype import DataEventType
    from .targetingdatastatus import TargetingDataStatus
    from .targetingdatauniques import TargetingDataUniques
    from .targetingdatauniquesv2 import TargetingDataUniquesV2


@dataclass
class TargetingData:
    """
    None
    """
    alwaysShowButIgnoreUniques: bool
    createdAt: Any
    creativeId: str
    dataEventType: Optional[DataEventType]
    dataName: str
    dataOwnerId: str
    dataOwnerTypeId: str
    dataTypeId: str
    displayNameOverride: str
    doNotUpdateUniques: bool
    id: str
    importanceRank: int
    isLegacyTrackingTag: bool
    recencyIsExternallyManaged: bool
    shouldTrackOriginalId: str
    supplyVendorId: str
    targetingDataStatus: Optional[TargetingDataStatus]
    targetingDataUniques: Optional[TargetingDataUniques]
    targetingDataUniquesV2: Optional[TargetingDataUniquesV2]
    testImportanceRank: int
    usedForFeatureTargeting: bool

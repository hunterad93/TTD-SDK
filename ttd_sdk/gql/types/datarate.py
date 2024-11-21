from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .dataratecard import DataRateCard
    from .dataratetype import DataRateType
    from .thirdpartydataconnection import ThirdPartyDataConnection


@dataclass
class DataRate:
    """
    None
    """
    baseDataRateId: str
    currencyCodeId: str
    dataRateCard: Optional[DataRateCard]
    dataRateLevelId: str
    dataRateType: Optional[DataRateType]
    id: str
    rateAmount: Any
    secondaryRateAmount: Any
    thirdPartyData: Optional[ThirdPartyDataConnection]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup


@dataclass
class AdGroupSpendSettingsMigrationData:
    """
    None
    """
    originalAdGroup: Optional[AdGroup]
    spendPriority: int

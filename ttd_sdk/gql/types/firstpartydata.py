from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .activeuniques import ActiveUniques
    from .advertiser import Advertiser


@dataclass
class FirstPartyData:
    """
    None
    """
    activeUniques: Optional[ActiveUniques]
    advertiser: Optional[Advertiser]
    id: int
    name: str

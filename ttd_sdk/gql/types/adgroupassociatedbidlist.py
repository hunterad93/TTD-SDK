from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ibidlist import IBidList


@dataclass
class AdGroupAssociatedBidList:
    """
    None
    """
    bidList: Optional[IBidList]
    isDefaultForUI: bool
    isEnabled: bool

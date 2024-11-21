from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bidline import BidLine
    from .bidlistadjustmenttype import BidListAdjustmentType
    from .bidlistdimension import BidListDimension
    from .bidlistowner import BidListOwner
    from .bidlistownertype import BidListOwnerType
    from .bidlistsource import BidListSource
    from .multiplematchresolutiontype import MultipleMatchResolutionType


@dataclass
class PublisherList:
    """
    None
    """
    id: str
    adjustmentType: Optional[BidListAdjustmentType]
    bidLines: List[Optional[BidLine]]
    bidLinesCount: int
    dimensions: List[Optional[BidListDimension]]
    isAvailableForLibraryUse: bool
    name: str
    owner: Optional[BidListOwner]
    ownerType: Optional[BidListOwnerType]
    resolutionType: Optional[MultipleMatchResolutionType]
    source: Optional[BidListSource]
    volumeControlOnly: bool

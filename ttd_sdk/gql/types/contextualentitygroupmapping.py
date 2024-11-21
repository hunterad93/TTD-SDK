from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bidlistadjustmenttype import BidListAdjustmentType
    from .contextualentitygroup import ContextualEntityGroup


@dataclass
class ContextualEntityGroupMapping:
    """
    Represents a contextual entity group in the contextual marketplace.
    """
    bidAdjustment: Any
    bidListAdjustmentType: Optional[BidListAdjustmentType]
    contextualEntityGroup: Optional[ContextualEntityGroup]
    contextualEntityGroupId: str
    contextualId: str
    isDeleted: bool
    ordering: int

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .prebidcategorystate import PreBidCategoryState
    from .prebidcategorytype import PreBidCategoryType


@dataclass
class PreBidContextualCategory:
    """
    Categories that can be used in the Pre-Bid Contextual Category bid dimension.
    """
    categoryType: Optional[PreBidCategoryType]
    id: str
    isReady: bool
    lastUpdateDateTime: Any
    name: str
    path: str
    referrerCategorySource: int
    scale: int
    state: Optional[PreBidCategoryState]

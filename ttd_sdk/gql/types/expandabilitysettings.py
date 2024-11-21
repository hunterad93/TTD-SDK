from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adexpansionaction import AdExpansionAction
    from .adexpansiondirection import AdExpansionDirection
    from .creativetechvendor import CreativeTechVendor


@dataclass
class ExpandabilitySettings:
    """
    None
    """
    creativeTechVendor: Optional[CreativeTechVendor]
    creativeTechVendorId: int
    expansionAction: Optional[AdExpansionAction]
    expansionDirection: int
    expansionDirections: List[Optional[AdExpansionDirection]]
    isExpandable: bool

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .thirdpartydatabrand import ThirdPartyDataBrand


@dataclass
class ThirdPartyDataBrandsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[ThirdPartyDataBrand]

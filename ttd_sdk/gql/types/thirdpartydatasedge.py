from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .thirdpartydata import ThirdPartyData


@dataclass
class ThirdPartyDatasEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[ThirdPartyData]

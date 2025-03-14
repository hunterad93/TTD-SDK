from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .thirdpartydataprovider import ThirdPartyDataProvider


@dataclass
class ThirdPartyDataProvidersEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[ThirdPartyDataProvider]

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vasterror import VastError


@dataclass
class ThirdPartyVideoVastInfo:
    """
    None
    """
    hasCompanions: bool
    maxVastVersion: str
    numberOfVastWrappers: int
    numberOfVpaidWrappers: int
    vastErrors: List[Optional[VastError]]

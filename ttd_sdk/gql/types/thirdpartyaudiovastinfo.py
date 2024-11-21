from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vasterror import VastError


@dataclass
class ThirdPartyAudioVastInfo:
    """
    None
    """
    vastErrors: List[Optional[VastError]]
    version: Any

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .daasterror import DaastError


@dataclass
class ThirdPartyAudioDaastInfo:
    """
    None
    """
    daastErrors: List[Optional[DaastError]]
    version: Any

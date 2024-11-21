from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .resolution import Resolution


@dataclass
class EncodingResolution:
    """
    None
    """
    max: Optional[Resolution]
    min: Optional[Resolution]

from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vasterrorcode import VastErrorCode


@dataclass
class VastError:
    """
    None
    """
    code: Optional[VastErrorCode]
    message: str

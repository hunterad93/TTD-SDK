from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .daasterrorcode import DaastErrorCode


@dataclass
class DaastError:
    """
    None
    """
    code: Optional[DaastErrorCode]
    message: str

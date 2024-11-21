from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .mediagenvendor import MediaGenVendor


@dataclass
class MediaGenServiceError:
    """
    None
    """
    field: List[str]
    message: str
    operationName: str
    vendor: Optional[MediaGenVendor]

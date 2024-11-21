from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .unprocessedcreative import UnprocessedCreative


@dataclass
class BulkCreativesApproveResult:
    """
    None
    """
    unprocessedCreatives: List[Optional[UnprocessedCreative]]

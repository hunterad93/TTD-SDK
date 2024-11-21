from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .programmatictilecontext import ProgrammaticTileContext
    from .programmatictiletype import ProgrammaticTileType


@dataclass
class ProgrammaticTile:
    """
    None
    """
    id: str
    isKoaOptimized: bool
    isUserOptimized: bool
    metadataSummaries: List[str]
    programmaticTileContext: Optional[ProgrammaticTileContext]
    type: Optional[ProgrammaticTileType]

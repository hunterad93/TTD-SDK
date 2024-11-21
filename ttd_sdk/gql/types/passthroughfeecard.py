from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .passthroughfeetarget import PassThroughFeeTarget
    from .passthroughfeetargettype import PassThroughFeeTargetType
    from .passthroughfeesconnection import PassThroughFeesConnection


@dataclass
class PassThroughFeeCard:
    """
    None
    """
    id: int
    passThroughFees: Optional[PassThroughFeesConnection]
    skipDateValidation: bool
    startDateUtc: Any
    target: Optional[PassThroughFeeTarget]
    targetType: Optional[PassThroughFeeTargetType]

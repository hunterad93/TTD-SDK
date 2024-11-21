from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .goalunit import GoalUnit
    from .roigoaltype import ROIGoalType


@dataclass
class Goal:
    """
    This type describes a campaign or ad group goal along with the current performance.
    """
    averageValue: Any
    isCustom: bool
    meetingPercentage: Any
    shortName: str
    target: Any
    type: Optional[ROIGoalType]
    unit: Optional[GoalUnit]

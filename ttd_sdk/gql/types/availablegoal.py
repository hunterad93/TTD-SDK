from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .goalunit import GoalUnit
    from .roigoaltype import ROIGoalType


@dataclass
class AvailableGoal:
    """
    This type describes a possible goal for a campaign or an ad group.
    """
    type: Optional[ROIGoalType]
    unit: Optional[GoalUnit]

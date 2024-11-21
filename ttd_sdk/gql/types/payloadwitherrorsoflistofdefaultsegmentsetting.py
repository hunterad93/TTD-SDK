from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .defaultsegmentsetting import DefaultSegmentSetting
    from .usererror import UserError


@dataclass
class PayloadWithErrorsOfListOfDefaultSegmentSetting:
    """
    Represents the executed state of a mutation, including all data and userErrors produced as a result of the operation.
    """
    data: List[Optional[DefaultSegmentSetting]]
    userErrors: List[Optional[UserError]]

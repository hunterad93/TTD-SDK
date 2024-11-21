from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .segmentruletype import SegmentRuleType


@dataclass
class DefaultSegmentSetting:
    """
    Represents the settings used (eg. recency window, rule type/value) for segments when segments are created by default.
    """
    eventName: str
    recencyWindowInDays: int
    segmentRuleType: Optional[SegmentRuleType]
    segmentRuleValue: Any

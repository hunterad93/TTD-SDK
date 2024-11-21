from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .defaulttrackingsetting import DefaultTrackingSetting
    from .defaulttrackingtagsetting import DefaultTrackingTagSetting


@dataclass
class Tracking:
    """
    None
    """
    defaultClickUrl: Optional[DefaultTrackingSetting]
    defaultThirdPartyTags: List[Optional[DefaultTrackingTagSetting]]
    defaultUrls: List[Optional[DefaultTrackingSetting]]

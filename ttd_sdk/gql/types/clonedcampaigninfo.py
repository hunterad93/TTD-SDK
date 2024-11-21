from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupclonepair import AdGroupClonePair
    from .campaign import Campaign


@dataclass
class ClonedCampaignInfo:
    """
    A cloned Campaign ID paired with AdGroup IDs that were cloned with it.
    """
    adGroupCloneMap: List[Optional[AdGroupClonePair]]
    campaignClone: Optional[Campaign]

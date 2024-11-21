from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .seed import Seed


@dataclass
class AdvertiserUpdateSeedForCampaignsResponse:
    """
    None
    """
    campaignIds: List[str]
    seed: Optional[Seed]

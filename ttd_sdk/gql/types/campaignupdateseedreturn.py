from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .campaign import Campaign


@dataclass
class CampaignUpdateSeedReturn:
    """
    None
    """
    campaign: Optional[Campaign]
    id: str

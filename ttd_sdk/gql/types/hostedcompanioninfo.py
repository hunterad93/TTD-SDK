from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .companioncreativesconnection import CompanionCreativesConnection


@dataclass
class HostedCompanionInfo:
    """
    None
    """
    companionCreatives: Optional[CompanionCreativesConnection]
    hasCompanions: bool

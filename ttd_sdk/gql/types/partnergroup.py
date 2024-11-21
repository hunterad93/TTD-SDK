from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .partnersconnection import PartnersConnection


@dataclass
class PartnerGroup:
    """
    None
    """
    id: str
    name: str
    partners: Optional[PartnersConnection]

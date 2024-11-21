from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .viewabilityfees import ViewabilityFees
    from .viewabilitysettings import ViewabilitySettings


@dataclass
class ViewabilityProvider:
    """
    None
    """
    displayName: str
    fees: Optional[ViewabilityFees]
    id: str
    isPartnerDefault: bool
    providerLogoUrl: str
    settings: Optional[ViewabilitySettings]

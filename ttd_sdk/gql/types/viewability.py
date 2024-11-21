from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .viewabilityprovider import ViewabilityProvider
    from .viewabilitysettings import ViewabilitySettings


@dataclass
class Viewability:
    """
    None
    """
    availableProviders: List[Optional[ViewabilityProvider]]
    selectedProviderId: str
    settingsOverride: Optional[ViewabilitySettings]

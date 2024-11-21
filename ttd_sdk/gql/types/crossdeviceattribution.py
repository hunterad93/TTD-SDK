from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .crossdeviceattributionconcept import CrossDeviceAttributionConcept


@dataclass
class CrossDeviceAttribution:
    """
    None
    """
    concept: Optional[CrossDeviceAttributionConcept]
    id: str
    name: str

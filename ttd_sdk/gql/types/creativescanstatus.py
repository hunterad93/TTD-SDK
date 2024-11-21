from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .rotationstate import RotationState


@dataclass
class CreativeScanStatus:
    """
    Metadata about creative scan. VAST / DAAST files of third party hosted creatives are scanned by creative scan periodically. Scan will update our internal representation of the creative, e.g. which version VAST spec it is using and what resolutions and bitrates are available.
    """
    lastScannedAt: Any
    lastScannedDate: Any
    rotationState: Optional[RotationState]

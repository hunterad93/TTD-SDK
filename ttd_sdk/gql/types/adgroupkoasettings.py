from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .koadimensions import KoaDimensions
    from .koaoptimizationsversion import KoaOptimizationsVersion


@dataclass
class AdGroupKoaSettings:
    """
    None
    """
    areFutureFeaturesEnabled: bool
    areFutureFeaturesEnabledForPartner: bool
    koaDimensions: Optional[KoaDimensions]
    minorVersion: str
    optimizationsVersion: Optional[KoaOptimizationsVersion]
    predictiveClearingEnabled: bool

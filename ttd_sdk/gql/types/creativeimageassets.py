from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creativeimageasset import CreativeImageAsset


@dataclass
class CreativeImageAssets:
    """
    None
    """
    icon: List[Optional[CreativeImageAsset]]
    logo: List[Optional[CreativeImageAsset]]
    main: List[Optional[CreativeImageAsset]]

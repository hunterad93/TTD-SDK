from dataclasses import dataclass
from typing import List

@dataclass
class AdvertiserValidationError:
    """
    None
    """
    field: List[str]
    message: str

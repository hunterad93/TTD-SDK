from dataclasses import dataclass
from typing import List

@dataclass
class AuthorizationError:
    """
    None
    """
    field: List[str]
    message: str

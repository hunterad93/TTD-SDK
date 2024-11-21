from dataclasses import dataclass
from typing import List

@dataclass
class UserError:
    """
    None
    """
    field: List[str]
    message: str

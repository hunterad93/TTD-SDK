from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .customlabel import CustomLabel


@dataclass
class CustomLabelsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[CustomLabel]

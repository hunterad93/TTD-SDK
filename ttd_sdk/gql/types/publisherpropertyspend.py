from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .country import Country


@dataclass
class PublisherPropertySpend:
    """
    None
    """
    country: Optional[Country]
    spend: Any

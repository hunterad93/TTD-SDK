from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .publisherpropertymapping import PublisherPropertyMapping


@dataclass
class PublisherPropertyMappingsEdge:
    """
    An edge in a connection.
    """
    cursor: str
    node: Optional[PublisherPropertyMapping]

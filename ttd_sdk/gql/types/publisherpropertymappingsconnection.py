from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pageinfo import PageInfo
    from .publisherpropertymapping import PublisherPropertyMapping
    from .publisherpropertymappingsedge import PublisherPropertyMappingsEdge


@dataclass
class PublisherPropertyMappingsConnection:
    """
    A connection to a list of items.
    """
    edges: List[Optional[PublisherPropertyMappingsEdge]]
    nodes: List[Optional[PublisherPropertyMapping]]
    pageInfo: Optional[PageInfo]
    totalCount: int

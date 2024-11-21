from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .publisher import Publisher
    from .publisherproperty import PublisherProperty


@dataclass
class PublisherPropertyMapping:
    """
    None
    """
    channel: str
    creationDate: Any
    id: int
    lastUpdateDate: Any
    lastUpdatedBy: str
    network: str
    pageUrlRegex: str
    publisherProperty: Optional[PublisherProperty]
    site: str
    supplyPublisher: Optional[Publisher]

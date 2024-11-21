from dataclasses import dataclass

@dataclass
class PageInfo:
    """
    Information about pagination in a connection.
    """
    endCursor: str
    hasNextPage: bool
    hasPreviousPage: bool
    startCursor: str

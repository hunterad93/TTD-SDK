from dataclasses import dataclass

@dataclass
class PrivateContract:
    """
    Private contract recommended to an adgroup or campaign
    """
    id: str
    availsCount: int

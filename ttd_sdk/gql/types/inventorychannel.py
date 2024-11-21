
from enum import Enum

class InventoryChannel(Enum):
    """
    Inventory channel
    """
    AUDIO = "AUDIO"
    DISPLAY = "DISPLAY"
    NATIVE_DISPLAY = "NATIVE_DISPLAY"
    NATIVE_VIDEO = "NATIVE_VIDEO"
    OTHER = "OTHER"
    OUT_OF_HOME = "OUT_OF_HOME"
    TV = "TV"
    VIDEO = "VIDEO"

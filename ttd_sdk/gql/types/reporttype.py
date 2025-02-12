
from enum import Enum

class ReportType(Enum):
    """
    None
    """
    AD_FORMAT = "AD_FORMAT"
    AD_GROUP = "AD_GROUP"
    AUDIENCE = "AUDIENCE"
    CONTEXTUAL = "CONTEXTUAL"
    CREATIVE = "CREATIVE"
    DEVICE_DETAILS = "DEVICE_DETAILS"
    FREQUENCY_AND_DISTRIBUTION = "FREQUENCY_AND_DISTRIBUTION"
    GEO = "GEO"
    INVENTORY_CONTROL_PUBLISHER = "INVENTORY_CONTROL_PUBLISHER"
    INVENTORY_SELECTION_PUBLISHER_AND_PMP = "INVENTORY_SELECTION_PUBLISHER_AND_PMP"
    LANGUAGE = "LANGUAGE"
    REACH_AND_FREQUENCY = "REACH_AND_FREQUENCY"
    RECENCY = "RECENCY"
    TIME_AND_DAY = "TIME_AND_DAY"
    VIEWABILITY = "VIEWABILITY"
    WEATHER = "WEATHER"

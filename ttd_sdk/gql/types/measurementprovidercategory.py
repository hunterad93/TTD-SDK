
from enum import Enum

class MeasurementProviderCategory(Enum):
    """
    Each measurement solution available within the platform falls under a single measurement provider category.
    """
    ALCOHOLIC_BEVERAGES = "ALCOHOLIC_BEVERAGES"
    AUTO_MEASUREMENT = "AUTO_MEASUREMENT"
    BRAND_LIFT = "BRAND_LIFT"
    FIRST_PARTY = "FIRST_PARTY"
    IN_APP = "IN_APP"
    LOCATION = "LOCATION"
    OFFLINE_SALES_MEASUREMENT = "OFFLINE_SALES_MEASUREMENT"
    OTHER = "OTHER"
    PHARMA = "PHARMA"
    REACH = "REACH"
    RETAIL = "RETAIL"
    THEATRICAL = "THEATRICAL"
    VIEWABILITY = "VIEWABILITY"
    WALMART_MEASUREMENT = "WALMART_MEASUREMENT"
    WEB_TRACKING_TAG = "WEB_TRACKING_TAG"

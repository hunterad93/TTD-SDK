
from enum import Enum

class SegmentRuleType(Enum):
    """
    The type of rule to apply that filters the segment by event frequency, monetary value, or top customers.
    """
    ABSOLUTE_FREQUENCY = "ABSOLUTE_FREQUENCY"
    ABSOLUTE_MONETARY_VALUE = "ABSOLUTE_MONETARY_VALUE"
    TOP_CUSTOMERS = "TOP_CUSTOMERS"

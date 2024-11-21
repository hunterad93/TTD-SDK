from dataclasses import dataclass

@dataclass
class RangeOfInt32:
    """
    A range of values. The range may be unbounded in either direction.
    """
    max: int
    min: int

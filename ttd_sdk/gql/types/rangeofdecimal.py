from dataclasses import dataclass

@dataclass
class RangeOfDecimal:
    """
    A range of values. The range may be unbounded in either direction.
    """
    max: Any
    min: Any

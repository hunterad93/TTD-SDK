from dataclasses import dataclass

@dataclass
class Currency:
    """
    None
    """
    decimalPlaces: Any
    id: str
    isVisible: bool
    name: str
    namePlural: str
    shouldPrefixCurrencySymbol: bool
    symbol: str

from dataclasses import dataclass

@dataclass
class SpecialPlatformFeatures:
    """
    Denotes which special platform features are applied to the parent entity.
    """
    hideDoohChannelBuyingInUi: bool

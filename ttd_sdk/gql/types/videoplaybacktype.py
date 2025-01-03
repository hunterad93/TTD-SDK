
from enum import Enum

class VideoPlaybackType(Enum):
    """
    None
    """
    ACCOMPANYING_CONTENT = "ACCOMPANYING_CONTENT"
    IN_ARTICLE = "IN_ARTICLE"
    IN_BANNER = "IN_BANNER"
    IN_FEED = "IN_FEED"
    INTERSTITIAL_SLIDER_FLOATING = "INTERSTITIAL_SLIDER_FLOATING"
    MID_ROLL = "MID_ROLL"
    NONE = "NONE"
    POST_ROLL = "POST_ROLL"
    PRE_ROLL = "PRE_ROLL"
    STANDALONE = "STANDALONE"
    UNDECLARED = "UNDECLARED"

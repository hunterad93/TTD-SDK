
from enum import Enum

class CampaignPacingMode(Enum):
    """
    None
    """
    PACE_AHEAD = "PACE_AHEAD"
    PACE_AS_SOON_AS_POSSIBLE = "PACE_AS_SOON_AS_POSSIBLE"
    PACE_EVENLY = "PACE_EVENLY"
    PACE_TO_DAILY_CAP = "PACE_TO_DAILY_CAP"

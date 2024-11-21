from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupflightmigrationdata import AdGroupFlightMigrationData
    from .campaignflight import CampaignFlight


@dataclass
class CampaignFlightMigrationData:
    """
    None
    """
    adGroupFlights: List[Optional[AdGroupFlightMigrationData]]
    originalCampaignFlight: Optional[CampaignFlight]

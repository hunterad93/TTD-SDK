from dataclasses import dataclass

@dataclass
class CreativeVideoAttributes:
    """
    None
    """
    clearCastClockNumber: str
    eventTrackingUrlsAreSecure: bool
    hasCompanions: bool
    hasEndCard: bool
    hasVpaid: bool
    id: str
    nonLinearOnly: bool
    numVastWrappers: int
    numVpaidWrappers: int
    universalAdIdRegistry: str
    vastErrors: int
    vastExceptionMessage: str
    vastVersion: int
    vpaidWrapperVendors: int

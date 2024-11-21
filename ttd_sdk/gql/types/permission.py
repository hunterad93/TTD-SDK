from dataclasses import dataclass

@dataclass
class Permission:
    """
    None
    """
    clientViewable: bool
    description: str
    engineeringContact: str
    expectedGADate: Any
    featureId: str
    id: str
    isSoxAudited: bool
    name: str
    notes: str
    permissionStageId: str
    pmContact: str
    slackChannel: str

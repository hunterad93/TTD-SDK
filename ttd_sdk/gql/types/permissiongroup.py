from dataclasses import dataclass

@dataclass
class PermissionGroup:
    """
    None
    """
    clientViewable: bool
    description: str
    id: str
    isGlobalPermissionGroup: bool
    isSoxAudited: bool
    isStandardRole: bool
    name: str
    partnerGroupId: str

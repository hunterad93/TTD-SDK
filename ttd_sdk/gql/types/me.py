from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .assignedpermissiongroupsconnection import AssignedPermissionGroupsConnection
    from .assignedpermissionsconnection import AssignedPermissionsConnection
    from .expandedthirdpartydatasegment import ExpandedThirdPartyDataSegment
    from .expandedthirdpartydatasegmentconnection import ExpandedThirdPartyDataSegmentConnection
    from .favoritedadvertisersconnection import FavoritedAdvertisersConnection
    from .partnergroup import PartnerGroup
    from .thirdpartydataconnection import ThirdPartyDataConnection
    from .thirdpartydataprovidersconnection import ThirdPartyDataProvidersConnection
    from .viewableusergroupsconnection import ViewableUserGroupsConnection


@dataclass
class Me:
    """
    None
    """
    assignedPermissionGroups: Optional[AssignedPermissionGroupsConnection]
    assignedPermissions: Optional[AssignedPermissionsConnection]
    expandedThirdPartyDataSegment: Optional[ExpandedThirdPartyDataSegmentConnection]
    expandedThirdPartyDataSegments: List[Optional[ExpandedThirdPartyDataSegment]]
    favoritedAdvertisers: Optional[FavoritedAdvertisersConnection]
    id: str
    partnerGroup: Optional[PartnerGroup]
    thirdPartyData: Optional[ThirdPartyDataConnection]
    thirdPartyDataProviders: Optional[ThirdPartyDataProvidersConnection]
    viewableUserGroups: Optional[ViewableUserGroupsConnection]

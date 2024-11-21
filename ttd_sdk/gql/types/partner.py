from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertisersconnection import AdvertisersConnection
    from .associatedbidlistsconnection import AssociatedBidListsConnection
    from .contextualentitiesconnection import ContextualEntitiesConnection
    from .contextualentitygroupsconnection import ContextualEntityGroupsConnection
    from .expandablefee import ExpandableFee
    from .geosegmentsconnection import GeoSegmentsConnection
    from .ownedbidlistsconnection import OwnedBidListsConnection
    from .partnergroup import PartnerGroup
    from .prebidcontextualcategoriesconnection import PreBidContextualCategoriesConnection
    from .specialplatformfeatures import SpecialPlatformFeatures


@dataclass
class Partner:
    """
    None
    """
    advertisers: Optional[AdvertisersConnection]
    chinaMSASigned: bool
    contextualEntities: Optional[ContextualEntitiesConnection]
    contextualEntityGroups: Optional[ContextualEntityGroupsConnection]
    expandableFee: Optional[ExpandableFee]
    geoSegments: Optional[GeoSegmentsConnection]
    id: str
    idInteger: int
    isPurchaseOrderNumberRequired: bool
    name: str
    partnerGroup: Optional[PartnerGroup]
    preBidContextualCategories: Optional[PreBidContextualCategoriesConnection]
    specialPlatformFeatures: Optional[SpecialPlatformFeatures]
    associatedBidLists: Optional[AssociatedBidListsConnection]
    ownedBidLists: Optional[OwnedBidListsConnection]

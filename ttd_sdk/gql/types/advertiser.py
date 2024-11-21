from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advertiseraudiencesettings import AdvertiserAudienceSettings
    from .advertiserreportsmetadata import AdvertiserReportsMetadata
    from .advertiservettingstatus import AdvertiserVettingStatus
    from .associatedbidlistsconnection import AssociatedBidListsConnection
    from .attribution import Attribution
    from .availablegoal import AvailableGoal
    from .brand import Brand
    from .campaignsconnection import CampaignsConnection
    from .contextualentitiesconnection import ContextualEntitiesConnection
    from .contextualentitygroupsconnection import ContextualEntityGroupsConnection
    from .conversionliftexperiment import ConversionLiftExperiment
    from .country import Country
    from .creativeissuesconnection import CreativeIssuesConnection
    from .creativesconnection import CreativesConnection
    from .currency import Currency
    from .customlabelsconnection import CustomLabelsConnection
    from .defaultbidlistsconnection import DefaultBidListsConnection
    from .defaultrightmediaoffer import DefaultRightMediaOffer
    from .dynamiccreativerule import DynamicCreativeRule
    from .firstpartydataconnection import FirstPartyDataConnection
    from .geosegmentsconnection import GeoSegmentsConnection
    from .industrycategory import IndustryCategory
    from .marketplace import Marketplace
    from .measurementprovidercategory import MeasurementProviderCategory
    from .ownedbidlistsconnection import OwnedBidListsConnection
    from .partner import Partner
    from .political import Political
    from .prebidcontextualcategoriesconnection import PreBidContextualCategoriesConnection
    from .programmatictile import ProgrammaticTile
    from .rightmediaoffertype import RightMediaOfferType
    from .seat import Seat
    from .seed import Seed
    from .specialplatformfeatures import SpecialPlatformFeatures
    from .tracking import Tracking
    from .trackingtagsconnection import TrackingTagsConnection
    from .viewability import Viewability
    from .viewabilitysettings import ViewabilitySettings


@dataclass
class Advertiser:
    """
    None
    """
    assignedBrands: List[Optional[Brand]]
    attribution: Optional[Attribution]
    audienceSettings: Optional[AdvertiserAudienceSettings]
    availableCountries: List[Optional[Country]]
    availableGoals: List[Optional[AvailableGoal]]
    availableIndustryCategories: List[Optional[IndustryCategory]]
    availableIndustrySubCategories: List[Optional[IndustryCategory]]
    brandOwner: str
    campaigns: Optional[CampaignsConnection]
    channelCount: int
    clickDedupeWindowInSeconds: int
    contextualEntities: Optional[ContextualEntitiesConnection]
    contextualEntityGroups: Optional[ContextualEntityGroupsConnection]
    conversionDeDupeWindowInSeconds: int
    conversionLiftExperiments: List[Optional[ConversionLiftExperiment]]
    country: Optional[Country]
    creativeIssues: Optional[CreativeIssuesConnection]
    creatives: Optional[CreativesConnection]
    currency: Optional[Currency]
    customLabels: Optional[CustomLabelsConnection]
    defaultPartnerViewabilitySettings: Optional[ViewabilitySettings]
    defaultRightMediaOffer: Optional[DefaultRightMediaOffer]
    defaultSeed: Optional[Seed]
    description: str
    domainAddress: str
    dynamicCreativeRules: List[Optional[DynamicCreativeRule]]
    firstPartyData: Optional[FirstPartyDataConnection]
    funnelLocationCount: int
    geoSegments: Optional[GeoSegmentsConnection]
    hasAvailableSeedPixels: bool
    id: str
    ignoreReferralUrlInConversion: bool
    industryCategory: Optional[IndustryCategory]
    industrySubCategory: Optional[IndustryCategory]
    isArchived: bool
    isBlockedFromHhSolution: bool
    isFavoriteForUser: bool
    isMarketplaceEnabledByDefault: bool
    isWithCampaignsAtRisk: bool
    isWithLiveCampaigns: bool
    keywords: List[str]
    logo: str
    marketplace: Optional[Marketplace]
    mostUsedSeed: Optional[Seed]
    name: str
    nameDSA: str
    partner: Optional[Partner]
    payerNameDSA: str
    political: Optional[Political]
    preBidContextualCategories: Optional[PreBidContextualCategoriesConnection]
    programmaticTiles: List[Optional[ProgrammaticTile]]
    rightMediaOfferTypes: List[Optional[RightMediaOfferType]]
    seats: List[Optional[Seat]]
    secretKey: str
    seeds: List[Optional[Seed]]
    specialPlatformFeatures: Optional[SpecialPlatformFeatures]
    suggestedMeasurementProviderCategories: List[Optional[MeasurementProviderCategory]]
    totalCampaignChannelCount: int
    totalFunnelLocationCount: int
    tracking: Optional[Tracking]
    trackingTags: Optional[TrackingTagsConnection]
    useImpressionsOnlyBudgeting: bool
    useMediaCostBasisForCampaignFees: bool
    vettingStatus: Optional[AdvertiserVettingStatus]
    viewability: Optional[Viewability]
    associatedBidLists: Optional[AssociatedBidListsConnection]
    defaultBidLists: Optional[DefaultBidListsConnection]
    ownedBidLists: Optional[OwnedBidListsConnection]
    reportsMetadata: Optional[AdvertiserReportsMetadata]

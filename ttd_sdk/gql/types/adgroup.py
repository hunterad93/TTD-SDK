from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupassociatedbidlistsconnection import AdGroupAssociatedBidListsConnection
    from .adgroupautooptimizationsettings import AdGroupAutoOptimizationSettings
    from .adgroupbudget import AdGroupBudget
    from .adgroupchannelspend import AdGroupChannelSpend
    from .adgroupchanneltype import AdGroupChannelType
    from .adgroupcreativesconnection import AdGroupCreativesConnection
    from .adgroupexpressiveness import AdGroupExpressiveness
    from .adgroupflight import AdGroupFlight
    from .adgroupflightsconnection import AdGroupFlightsConnection
    from .adgroupfunnellocationtype import AdGroupFunnelLocationType
    from .adgroupkoasettings import AdGroupKoaSettings
    from .adgroupreportsmetadata import AdGroupReportsMetadata
    from .adgroupspend import AdGroupSpend
    from .advertiser import Advertiser
    from .appliedbidlistsconnection import AppliedBidListsConnection
    from .campaign import Campaign
    from .campaignflightsconnection import CampaignFlightsConnection
    from .creativeissuesconnection import CreativeIssuesConnection
    from .creativesconnection import CreativesConnection
    from .customlabelsconnection import CustomLabelsConnection
    from .goal import Goal
    from .impressionfrequencycountersconnection import ImpressionFrequencyCountersConnection
    from .industrycategory import IndustryCategory
    from .markettype import MarketType
    from .marketplace import Marketplace
    from .nielsentrackingattributes import NielsenTrackingAttributes
    from .ownedbidlistsconnection import OwnedBidListsConnection
    from .partner import Partner
    from .programmatictile import ProgrammaticTile
    from .qualityallianceviewabilityprofiletype import QualityAllianceViewabilityProfileType
    from .retailerbrandrestrictions import RetailerBrandRestrictions
    from .valueaddedprovider import ValueAddedProvider
    from .viewabilitystandardtype import ViewabilityStandardType


@dataclass
class AdGroup:
    """
    None
    """
    adgroupCreatives: Optional[AdGroupCreativesConnection]
    adGroupFlights: Optional[AdGroupFlightsConnection]
    advertiser: Optional[Advertiser]
    autoOptimizationSettings: Optional[AdGroupAutoOptimizationSettings]
    availableIndustryCategories: List[Optional[IndustryCategory]]
    availableIndustrySubCategories: List[Optional[IndustryCategory]]
    baseBidCPMInAdvertiserCurrency: Any
    budget: Optional[AdGroupBudget]
    budgetInAdvertiserCurrency: Any
    budgetInImpressions: Any
    campaign: Optional[Campaign]
    campaignFlights: Optional[CampaignFlightsConnection]
    campaignStackRank: int
    channel: Optional[AdGroupChannelType]
    createdAt: Any
    creativeIssues: Optional[CreativeIssuesConnection]
    creatives: Optional[CreativesConnection]
    currentFlight: Optional[AdGroupFlight]
    customLabels: Optional[CustomLabelsConnection]
    dealsPresent: bool
    description: str
    displayViewabilityStandardIntegral: Optional[ViewabilityStandardType]
    expressiveness: Optional[AdGroupExpressiveness]
    funnelLocation: Optional[AdGroupFunnelLocationType]
    funnelLocationType: Optional[AdGroupFunnelLocationType]
    goal: Optional[Goal]
    id: str
    impressionFrequencyCounters: Optional[ImpressionFrequencyCountersConnection]
    industryCategory: Optional[IndustryCategory]
    industrySubCategory: Optional[IndustryCategory]
    isArchived: bool
    isDimensionalBiddingMode: bool
    isEnabled: bool
    isHighFillRate: bool
    isProgrammaticGuaranteed: bool
    isTemplate: bool
    koaSettings: Optional[AdGroupKoaSettings]
    lastUpdated: Any
    marketplace: Optional[Marketplace]
    marketType: Optional[MarketType]
    maxBidCPMInAdvertiserCurrency: Any
    name: str
    nielsenTrackingAttributes: Optional[NielsenTrackingAttributes]
    pacingGrainId: int
    partner: Optional[Partner]
    privateContractDefaultAdjustment: Any
    programmaticTiles: List[Optional[ProgrammaticTile]]
    qualityAllianceViewabilityProfile: Optional[QualityAllianceViewabilityProfileType]
    restrictions: List[Optional[RetailerBrandRestrictions]]
    spend: Optional[AdGroupSpend]
    spendPerChannel: List[Optional[AdGroupChannelSpend]]
    valueAddedProviders: List[Optional[ValueAddedProvider]]
    videoViewabilityStandardIntegral: Optional[ViewabilityStandardType]
    appliedBidLists: Optional[AppliedBidListsConnection]
    associatedBidLists: Optional[AdGroupAssociatedBidListsConnection]
    ownedBidLists: Optional[OwnedBidListsConnection]
    reportsMetadata: Optional[AdGroupReportsMetadata]

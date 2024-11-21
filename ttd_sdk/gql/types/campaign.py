from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroupsconnection import AdGroupsConnection
    from .advertiser import Advertiser
    from .associatedbidlistsconnection import AssociatedBidListsConnection
    from .audience import Audience
    from .campaignbudget import CampaignBudget
    from .campaignbudgetmigrationreports import CampaignBudgetMigrationReports
    from .campaignbudgetmigrationstatus import CampaignBudgetMigrationStatus
    from .campaignchanneltype import CampaignChannelType
    from .campaignflight import CampaignFlight
    from .campaignobjective import CampaignObjective
    from .campaignpacingmode import CampaignPacingMode
    from .campaignpacingsettings import CampaignPacingSettings
    from .campaignreporting import CampaignReporting
    from .campaignreportsmetadata import CampaignReportsMetadata
    from .campaignspend import CampaignSpend
    from .campaigntype import CampaignType
    from .campaignversion import CampaignVersion
    from .conversionreportingcolumnsconnection import ConversionReportingColumnsConnection
    from .creativeissuesconnection import CreativeIssuesConnection
    from .customcpatype import CustomCPAType
    from .customlabelsconnection import CustomLabelsConnection
    from .customroastype import CustomROASType
    from .defaultbidlistsconnection import DefaultBidListsConnection
    from .flightsconnection import FlightsConnection
    from .goal import Goal
    from .increment import Increment
    from .ownedbidlistsconnection import OwnedBidListsConnection
    from .partner import Partner
    from .passthroughfeecardsconnection import PassThroughFeeCardsConnection
    from .programmatictile import ProgrammaticTile
    from .seed import Seed
    from .sharetype import ShareType
    from .valueaddedprovider import ValueAddedProvider


@dataclass
class Campaign:
    """
    None
    """
    activeAdGroupCount: int
    adGroups: Optional[AdGroupsConnection]
    advertiser: Optional[Advertiser]
    audience: Optional[Audience]
    autoAllocatorEnabled: bool
    autoCampaignCapEnabled: bool
    autoPrioritizationEnabled: bool
    budget: Optional[CampaignBudget]
    budgetInImpressions: Any
    budgetMigrationReports: Optional[CampaignBudgetMigrationReports]
    budgetMigrationStatus: Optional[CampaignBudgetMigrationStatus]
    campaignPacingSettings: Optional[CampaignPacingSettings]
    channelType: Optional[CampaignChannelType]
    conversionReportingColumns: Optional[ConversionReportingColumnsConnection]
    createdAt: Any
    createdAtUtc: Any
    creativeIssues: Optional[CreativeIssuesConnection]
    currentFlight: Optional[CampaignFlight]
    currentOrNextFlight: Optional[CampaignFlight]
    customCPAClickWeight: Any
    customCPAType: Optional[CustomCPAType]
    customCPAViewthroughWeight: Any
    customLabels: Optional[CustomLabelsConnection]
    customROASType: Optional[CustomROASType]
    description: str
    endDate: Any
    flights: Optional[FlightsConnection]
    funnelLocationCount: int
    goal: Optional[Goal]
    id: str
    impressionsOnlyBudgetingCPM: Any
    increments: List[Optional[Increment]]
    ioContractId: int
    isArchived: bool
    isManagedByTTD: bool
    isMigratedToKokai: bool
    isProgrammaticGuaranteed: bool
    isTemplate: bool
    lastUpdated: Any
    lastUpdatedAtUtc: Any
    minimumAdGroupSpendInAdvertiserCurrency: Any
    name: str
    nextFlight: Optional[CampaignFlight]
    objective: Optional[CampaignObjective]
    pacingMode: Optional[CampaignPacingMode]
    pacingToEndOfFlightDailyRate: Any
    partner: Optional[Partner]
    partnerCostPercentageFee: Any
    passThroughFeeCards: Optional[PassThroughFeeCardsConnection]
    programmaticTiles: List[Optional[ProgrammaticTile]]
    purchaseOrderNumber: str
    seed: Optional[Seed]
    shareType: Optional[ShareType]
    siteUrl: str
    spend: Optional[CampaignSpend]
    startDate: Any
    timeZone: str
    timeZoneIANA: Any
    totalAdGroupCount: int
    type: Optional[CampaignType]
    valueAddedProviders: List[Optional[ValueAddedProvider]]
    version: Optional[CampaignVersion]
    associatedBidLists: Optional[AssociatedBidListsConnection]
    defaultBidLists: Optional[DefaultBidListsConnection]
    ownedBidLists: Optional[OwnedBidListsConnection]
    reporting: Optional[CampaignReporting]
    reportsMetadata: Optional[CampaignReportsMetadata]

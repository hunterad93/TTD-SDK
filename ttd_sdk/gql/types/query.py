from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adgroup import AdGroup
    from .adgroupsconnection import AdGroupsConnection
    from .adgroupswithproblematicchannelconnection import AdGroupsWithProblematicChannelConnection
    from .advertiser import Advertiser
    from .advertisersconnection import AdvertisersConnection
    from .audience import Audience
    from .audiencesconnection import AudiencesConnection
    from .baserecommendation import BaseRecommendation
    from .budgetestimationresponse import BudgetEstimationResponse
    from .bulkapijob import BulkApiJob
    from .campaign import Campaign
    from .campaignclonecampaignlevelforecastresult import CampaignCloneCampaignLevelForecastResult
    from .campaigncloneinventoryrecommendation import CampaignCloneInventoryRecommendation
    from .campaigncloneinventoryrecommendationadgroup import CampaignCloneInventoryRecommendationAdGroup
    from .campaigncloneinventoryrecommendationpropertylevelforecastresult import CampaignCloneInventoryRecommendationPropertyLevelForecastResult
    from .campaigncloneprogress import CampaignCloneProgress
    from .campaigncloneprogressesconnection import CampaignCloneProgressesConnection
    from .campaignset import CampaignSet
    from .campaignsconnection import CampaignsConnection
    from .categoryprovider import CategoryProvider
    from .contextualentitiesconnection import ContextualEntitiesConnection
    from .contextualentity import ContextualEntity
    from .creative import Creative
    from .creativeissuesconnection import CreativeIssuesConnection
    from .creativesconnection import CreativesConnection
    from .defaultsegmentsetting import DefaultSegmentSetting
    from .forecast import Forecast
    from .forecastsforadvertiserconnection import ForecastsForAdvertiserConnection
    from .geosegmentssearchconnection import GeoSegmentsSearchConnection
    from .helptext import HelpText
    from .ibidlist import IBidList
    from .jobprogress import JobProgress
    from .me import Me
    from .omnichannelforecastrecommendation import OmnichannelForecastRecommendation
    from .omnichannelgroupconversionpath import OmnichannelGroupConversionPath
    from .omnichannelgrouptrackingtag import OmnichannelGroupTrackingTag
    from .partner import Partner
    from .partnergroup import PartnerGroup
    from .partnergroupsconnection import PartnerGroupsConnection
    from .partnersconnection import PartnersConnection
    from .payloadwitherrorsoflistofprogrammatictilereportmetadataresponse import PayloadWithErrorsOfListOfProgrammaticTileReportMetadataResponse
    from .permission import Permission
    from .permissiongroup import PermissionGroup
    from .permissiongroupsconnection import PermissionGroupsConnection
    from .permissionsconnection import PermissionsConnection
    from .prebidcontextualcategory import PreBidContextualCategory
    from .referrercategorysource import ReferrerCategorySource
    from .referrercategorysourcesconnection import ReferrerCategorySourcesConnection
    from .reporttypemodel import ReportTypeModel
    from .scheduledreportjobstatusresponse import ScheduledReportJobStatusResponse
    from .seed import Seed
    from .thirdpartydata import ThirdPartyData
    from .thirdpartydatadelta import ThirdPartyDataDelta
    from .thirdpartydataprovider import ThirdPartyDataProvider
    from .thirdpartydataprovidersconnection import ThirdPartyDataProvidersConnection
    from .thirdpartydatasconnection import ThirdPartyDatasConnection
    from .trackingtag import TrackingTag
    from .universalpixel import UniversalPixel
    from .universalpixelsconnection import UniversalPixelsConnection
    from .userassignedpermissiongroupsconnection import UserAssignedPermissionGroupsConnection
    from .userassignedpermissionsconnection import UserAssignedPermissionsConnection


@dataclass
class Query:
    """
    None
    """
    adGroup: Optional[AdGroup]
    adGroups: Optional[AdGroupsConnection]
    adGroupsWithProblematicChannel: Optional[AdGroupsWithProblematicChannelConnection]
    advertiser: Optional[Advertiser]
    advertisers: Optional[AdvertisersConnection]
    audience: Optional[Audience]
    audiences: Optional[AudiencesConnection]
    bulkAdGroup: Optional[BulkApiJob]
    bulkCampaign: Optional[BulkApiJob]
    bulkCampaignFlights: Optional[BulkApiJob]
    bulkCampaignSets: Optional[BulkApiJob]
    campaign: Optional[Campaign]
    campaignCloneProgress: Optional[CampaignCloneProgress]
    campaignCloneProgresses: Optional[CampaignCloneProgressesConnection]
    campaigns: Optional[CampaignsConnection]
    campaignSet: Optional[CampaignSet]
    contextualEntities: Optional[ContextualEntitiesConnection]
    contextualEntity: Optional[ContextualEntity]
    creative: Optional[Creative]
    creativeIssues: Optional[CreativeIssuesConnection]
    creatives: Optional[CreativesConnection]
    geoSegmentsSearch: Optional[GeoSegmentsSearchConnection]
    helpText: Optional[HelpText]
    jobProgress: Optional[JobProgress]
    me: Optional[Me]
    omnichannelForecastRecommendation: List[Optional[OmnichannelForecastRecommendation]]
    omnichannelGroupConversionPaths: List[Optional[OmnichannelGroupConversionPath]]
    omnichannelGroupTrackingTags: List[Optional[OmnichannelGroupTrackingTag]]
    partner: Optional[Partner]
    partnerGroup: Optional[PartnerGroup]
    partnerGroups: Optional[PartnerGroupsConnection]
    partners: Optional[PartnersConnection]
    permission: Optional[Permission]
    permissionGroup: Optional[PermissionGroup]
    permissionGroups: Optional[PermissionGroupsConnection]
    permissions: Optional[PermissionsConnection]
    pgAdGroupBudgetEstimation: Optional[BudgetEstimationResponse]
    preBidContextualCategory: Optional[PreBidContextualCategory]
    referrerCategorySource: Optional[ReferrerCategorySource]
    referrerCategorySources: Optional[ReferrerCategorySourcesConnection]
    seed: Optional[Seed]
    thirdPartyData: Optional[ThirdPartyData]
    thirdPartyDataDelta: Optional[ThirdPartyDataDelta]
    thirdPartyDataProvider: Optional[ThirdPartyDataProvider]
    thirdPartyDataProviders: Optional[ThirdPartyDataProvidersConnection]
    thirdPartyDatas: Optional[ThirdPartyDatasConnection]
    trackingTag: Optional[TrackingTag]
    universalPixel: Optional[UniversalPixel]
    universalPixels: Optional[UniversalPixelsConnection]
    userAssignedPermissionGroups: Optional[UserAssignedPermissionGroupsConnection]
    userAssignedPermissions: Optional[UserAssignedPermissionsConnection]
    bidList: Optional[IBidList]
    forecast: Optional[Forecast]
    forecasts: List[Optional[Forecast]]
    forecastsForAdvertiser: Optional[ForecastsForAdvertiserConnection]
    categoryProvider: Optional[CategoryProvider]
    defaultSegmentSettings: List[Optional[DefaultSegmentSetting]]
    isSegmentExpansionEnabled: bool
    campaignCloneCampaignLevelForecast: Optional[CampaignCloneCampaignLevelForecastResult]
    campaignCloneInventoryRecommendationAdGroup: Optional[CampaignCloneInventoryRecommendationAdGroup]
    campaignCloneInventoryRecommendationPropertyLevelForecasts: List[Optional[CampaignCloneInventoryRecommendationPropertyLevelForecastResult]]
    campaignCloneInventoryRecommendations: Optional[CampaignCloneInventoryRecommendation]
    recommendations: List[Optional[BaseRecommendation]]
    programmaticTileReportMetadata: Optional[PayloadWithErrorsOfListOfProgrammaticTileReportMetadataResponse]
    reportTypes: List[Optional[ReportTypeModel]]
    scheduledReportJobStatus: Optional[ScheduledReportJobStatusResponse]

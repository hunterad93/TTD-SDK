from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .categoryprovider import CategoryProvider
    from .fileinfo import FileInfo
    from .payloadwitherrorsofadgroup import PayloadWithErrorsOfAdGroup
    from .payloadwitherrorsofadvertiser import PayloadWithErrorsOfAdvertiser
    from .payloadwitherrorsofadvertiserupdateseedforcampaignsresponse import PayloadWithErrorsOfAdvertiserUpdateSeedForCampaignsResponse
    from .payloadwitherrorsofbulkapijob import PayloadWithErrorsOfBulkApiJob
    from .payloadwitherrorsofbulkcreativesapproveresult import PayloadWithErrorsOfBulkCreativesApproveResult
    from .payloadwitherrorsofcampaign import PayloadWithErrorsOfCampaign
    from .payloadwitherrorsofcampaignbudgetsettingsupdatereturn import PayloadWithErrorsOfCampaignBudgetSettingsUpdateReturn
    from .payloadwitherrorsofcampaignflight import PayloadWithErrorsOfCampaignFlight
    from .payloadwitherrorsofcampaignflightdeletereturn import PayloadWithErrorsOfCampaignFlightDeleteReturn
    from .payloadwitherrorsofcampaignupdateseedreturn import PayloadWithErrorsOfCampaignUpdateSeedReturn
    from .payloadwitherrorsofcreative import PayloadWithErrorsOfCreative
    from .payloadwitherrorsofcreativevideoattributes import PayloadWithErrorsOfCreativeVideoAttributes
    from .payloadwitherrorsofdownloadablereportexecuteresponse import PayloadWithErrorsOfDownloadableReportExecuteResponse
    from .payloadwitherrorsofforecast import PayloadWithErrorsOfForecast
    from .payloadwitherrorsofforecastsettingsupdate import PayloadWithErrorsOfForecastSettingsUpdate
    from .payloadwitherrorsofibidlist import PayloadWithErrorsOfIBidList
    from .payloadwitherrorsoflistofcampaigncloneprogress import PayloadWithErrorsOfListOfCampaignCloneProgress
    from .payloadwitherrorsoflistofcampaignversionupgradereturn import PayloadWithErrorsOfListOfCampaignVersionUpgradeReturn
    from .payloadwitherrorsoflistofdefaultsegmentsetting import PayloadWithErrorsOfListOfDefaultSegmentSetting
    from .payloadwitherrorsofpartner import PayloadWithErrorsOfPartner
    from .payloadwitherrorsofseed import PayloadWithErrorsOfSeed
    from .payloadwitherrorsofseedcreatereturn import PayloadWithErrorsOfSeedCreateReturn
    from .payloadwitherrorsofsubmitcreativeforapprovaloutput import PayloadWithErrorsOfSubmitCreativeForApprovalOutput


@dataclass
class Mutation:
    """
    None
    """
    adGroupUpdate: Optional[PayloadWithErrorsOfAdGroup]
    advertiserSetDefaultSeed: Optional[PayloadWithErrorsOfAdvertiser]
    advertiserUpdateSeedForCampaigns: Optional[PayloadWithErrorsOfAdvertiserUpdateSeedForCampaignsResponse]
    approveCreative: Optional[PayloadWithErrorsOfCreative]
    bulkApproveCreatives: Optional[PayloadWithErrorsOfBulkCreativesApproveResult]
    bulkCreateAdGroups: Optional[PayloadWithErrorsOfBulkApiJob]
    bulkCreateCampaignFlights: Optional[PayloadWithErrorsOfBulkApiJob]
    bulkCreateCampaigns: Optional[PayloadWithErrorsOfBulkApiJob]
    bulkCreateCampaignSets: Optional[PayloadWithErrorsOfBulkApiJob]
    bulkUpdateAdGroups: Optional[PayloadWithErrorsOfBulkApiJob]
    bulkUpdateCampaignFlights: Optional[PayloadWithErrorsOfBulkApiJob]
    bulkUpdateCampaigns: Optional[PayloadWithErrorsOfBulkApiJob]
    bulkUpdateCampaignSets: Optional[PayloadWithErrorsOfBulkApiJob]
    campaignBudgetSettingsUpdate: Optional[PayloadWithErrorsOfCampaignBudgetSettingsUpdateReturn]
    campaignClonesCreate: Optional[PayloadWithErrorsOfListOfCampaignCloneProgress]
    campaignCreate: Optional[PayloadWithErrorsOfCampaign]
    campaignFlightCreate: Optional[PayloadWithErrorsOfCampaignFlight]
    campaignFlightDelete: Optional[PayloadWithErrorsOfCampaignFlightDeleteReturn]
    campaignFlightUpdate: Optional[PayloadWithErrorsOfCampaignFlight]
    campaignUpdate: Optional[PayloadWithErrorsOfCampaign]
    campaignUpdateSeed: Optional[PayloadWithErrorsOfCampaignUpdateSeedReturn]
    campaignVersionUpgrade: Optional[PayloadWithErrorsOfListOfCampaignVersionUpgradeReturn]
    creativeUpdate: Optional[PayloadWithErrorsOfCreative]
    creativeVideoAttributesSetAdClearanceId: Optional[PayloadWithErrorsOfCreativeVideoAttributes]
    fileUpload: Optional[FileInfo]
    seedCreate: Optional[PayloadWithErrorsOfSeedCreateReturn]
    seedUpdate: Optional[PayloadWithErrorsOfSeed]
    submitCreativeForApproval: Optional[PayloadWithErrorsOfSubmitCreativeForApprovalOutput]
    adGroupAssociateBidList: Optional[PayloadWithErrorsOfAdGroup]
    advertiserAssociateBidList: Optional[PayloadWithErrorsOfAdvertiser]
    advertiserAssociateDefaultBidList: Optional[PayloadWithErrorsOfAdvertiser]
    bidListCreate: Optional[PayloadWithErrorsOfIBidList]
    bidListSet: Optional[PayloadWithErrorsOfIBidList]
    bidListUpdate: Optional[PayloadWithErrorsOfIBidList]
    campaignAssociateBidList: Optional[PayloadWithErrorsOfCampaign]
    campaignAssociateDefaultBidList: Optional[PayloadWithErrorsOfCampaign]
    partnerAssociateBidList: Optional[PayloadWithErrorsOfPartner]
    forecastArchive: Optional[PayloadWithErrorsOfForecast]
    forecastClone: Optional[PayloadWithErrorsOfForecast]
    forecastCreate: Optional[PayloadWithErrorsOfForecast]
    forecastSettingsUpdate: Optional[PayloadWithErrorsOfForecastSettingsUpdate]
    categoryProviderUpdate: Optional[CategoryProvider]
    defaultSegmentSettingBatchCreate: Optional[PayloadWithErrorsOfListOfDefaultSegmentSetting]
    defaultSegmentSettingBatchDelete: Optional[PayloadWithErrorsOfListOfDefaultSegmentSetting]
    adGroupReportExecute: Optional[PayloadWithErrorsOfDownloadableReportExecuteResponse]
    advertiserReportExecute: Optional[PayloadWithErrorsOfDownloadableReportExecuteResponse]
    campaignReportExecute: Optional[PayloadWithErrorsOfDownloadableReportExecuteResponse]
    downloadableReportExecute: Optional[PayloadWithErrorsOfDownloadableReportExecuteResponse]

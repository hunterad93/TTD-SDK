from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .adloadcategory import AdLoadCategory
    from .adstxtsellertype import AdsTxtSellerType
    from .atmosphericcondition import AtmosphericCondition
    from .audiencereachpercentagetier import AudienceReachPercentageTier
    from .browser import Browser
    from .carrier import Carrier
    from .contentduration import ContentDuration
    from .contentrating import ContentRating
    from .contenttransparency import ContentTransparency
    from .contextualappcategory import ContextualAppCategory
    from .contextualsupplyvendorcategory import ContextualSupplyVendorCategory
    from .contextualsupplyvendorgenre import ContextualSupplyVendorGenre
    from .devicemodel import DeviceModel
    from .devicetype import DeviceType
    from .digitaloutofhomevenuetype import DigitalOutOfHomeVenueType
    from .domainclass import DomainClass
    from .doubleverifybrandsafetycategory import DoubleVerifyBrandSafetyCategory
    from .doubleverifycontextualcategory import DoubleVerifyContextualCategory
    from .factualproximitytarget import FactualProximityTarget
    from .firstpartydata import FirstPartyData
    from .frequencyadjustment import FrequencyAdjustment
    from .frequencylegacyadjustment import FrequencyLegacyAdjustment
    from .fullreferrerurl import FullReferrerUrl
    from .genre import Genre
    from .geosegment import GeoSegment
    from .idiosyncraticsegment import IdiosyncraticSegment
    from .integralbrandsafetycategory import IntegralBrandSafetyCategory
    from .integralcontextualcategory import IntegralContextualCategory
    from .integralpagequalitycategory import IntegralPageQualityCategory
    from .integralvideobrandsafetycategory import IntegralVideoBrandSafetyCategory
    from .integralvideopagequalitycategory import IntegralVideoPageQualityCategory
    from .integralviewabilitycategory import IntegralViewabilityCategory
    from .internetconnectiontype import InternetConnectionType
    from .likelyrefreshrate import LikelyRefreshRate
    from .livestream import Livestream
    from .markettypebidlist import MarketTypeBidList
    from .marketplace import Marketplace
    from .nativecontexttype import NativeContextType
    from .nativeplacementtype import NativePlacementType
    from .operatingsystem import OperatingSystem
    from .peer39brandsafetycategory import Peer39BrandSafetyCategory
    from .peer39contextualcategory import Peer39ContextualCategory
    from .peer39language import Peer39Language
    from .peer39pagequalitycategory import Peer39PageQualityCategory
    from .peer39viewabilitycategory import Peer39ViewabilityCategory
    from .placementpositionrelativetofold import PlacementPositionRelativeToFold
    from .productionquality import ProductionQuality
    from .publisher import Publisher
    from .rangeofdecimal import RangeOfDecimal
    from .rangeofint32 import RangeOfInt32
    from .renderingcontext import RenderingContext
    from .seller import Seller
    from .semasiocontextualcategory import SemasioContextualCategory
    from .supplypathoptimizationlist import SupplyPathOptimizationList
    from .supplyvendor import SupplyVendor
    from .ttdcontextualcategory import TTDContextualCategory
    from .ttdlanguage import TTDLanguage
    from .thirdpartydata import ThirdPartyData
    from .universalcategorytaxonomy import UniversalCategoryTaxonomy
    from .videomutedstate import VideoMutedState
    from .videoplaybacktype import VideoPlaybackType
    from .videoplayersize import VideoPlayerSize
    from .videoquality import VideoQuality
    from .videoskippability import VideoSkippability
    from .volumecontrolpriority import VolumeControlPriority
    from .weathercondition import WeatherCondition


@dataclass
class BidLine:
    """
    None
    """
    adLoadCategory: Optional[AdLoadCategory]
    adsTxtSellerType: Optional[AdsTxtSellerType]
    atmosphericCondition: Optional[AtmosphericCondition]
    audienceReachPercentageTier: Optional[AudienceReachPercentageTier]
    bidAdjustment: Any
    browser: Optional[Browser]
    carrier: Optional[Carrier]
    contentDuration: Optional[ContentDuration]
    contentRating: Optional[ContentRating]
    contentTransparency: Optional[ContentTransparency]
    contextualAppCategory: Optional[ContextualAppCategory]
    contextualSupplyVendorCategory: Optional[ContextualSupplyVendorCategory]
    contextualSupplyVendorGenre: Optional[ContextualSupplyVendorGenre]
    deviceModel: Optional[DeviceModel]
    deviceType: Optional[DeviceType]
    digitalOutOfHomeVenueType: Optional[DigitalOutOfHomeVenueType]
    displayViewabilityScoreRange: Optional[RangeOfDecimal]
    domainClass: Optional[DomainClass]
    domainFragment: str
    doubleVerifyBrandSafetyCategory: Optional[DoubleVerifyBrandSafetyCategory]
    doubleVerifyContextualCategory: Optional[DoubleVerifyContextualCategory]
    factualProximityTarget: Optional[FactualProximityTarget]
    firstPartyData: Optional[FirstPartyData]
    frequencyAdjustment: Optional[FrequencyAdjustment]
    frequencyLegacyAdjustment: Optional[FrequencyLegacyAdjustment]
    fullReferrerUrl: Optional[FullReferrerUrl]
    genre: Optional[Genre]
    geoSegment: Optional[GeoSegment]
    hourOfWeek: Any
    idiosyncraticSegment: Optional[IdiosyncraticSegment]
    integralBrandSafetyCategory: Optional[IntegralBrandSafetyCategory]
    integralContextualCategory: Optional[IntegralContextualCategory]
    integralPageQualityCategory: Optional[IntegralPageQualityCategory]
    integralVideoBrandSafetyCategory: Optional[IntegralVideoBrandSafetyCategory]
    integralVideoPageQualityCategory: Optional[IntegralVideoPageQualityCategory]
    integralViewabilityCategory: Optional[IntegralViewabilityCategory]
    internetConnectionType: Optional[InternetConnectionType]
    likelyRefreshRate: Optional[LikelyRefreshRate]
    livestream: Optional[Livestream]
    marketplace: Optional[Marketplace]
    marketType: Optional[MarketTypeBidList]
    nativeContextType: Optional[NativeContextType]
    nativePlacementType: Optional[NativePlacementType]
    operatingSystem: Optional[OperatingSystem]
    peer39BrandSafetyCategory: Optional[Peer39BrandSafetyCategory]
    peer39ContextualCategory: Optional[Peer39ContextualCategory]
    peer39Language: Optional[Peer39Language]
    peer39PageQualityCategory: Optional[Peer39PageQualityCategory]
    peer39ViewabilityCategory: Optional[Peer39ViewabilityCategory]
    placementPositionRelativeToFold: Optional[PlacementPositionRelativeToFold]
    productionQuality: Optional[ProductionQuality]
    publisher: Optional[Publisher]
    qualityScoreRange: Optional[RangeOfDecimal]
    recencyWindowInMinutes: Optional[RangeOfInt32]
    renderingContext: Optional[RenderingContext]
    seller: Optional[Seller]
    semasioContextualCategory: Optional[SemasioContextualCategory]
    supplyPathOptimizationList: Optional[SupplyPathOptimizationList]
    supplyVendor: Optional[SupplyVendor]
    temperatureBucketInCelsius: Optional[RangeOfDecimal]
    thirdPartyData: Optional[ThirdPartyData]
    ttdContextualCategory: Optional[TTDContextualCategory]
    ttdLanguage: Optional[TTDLanguage]
    universalCategoryTaxonomy: Optional[UniversalCategoryTaxonomy]
    videoCompletionRateScoreRange: Optional[RangeOfDecimal]
    videoMutedState: Optional[VideoMutedState]
    videoPlaybackType: Optional[VideoPlaybackType]
    videoPlayerSize: Optional[VideoPlayerSize]
    videoQuality: Optional[VideoQuality]
    videoSkippability: Optional[VideoSkippability]
    videoTruthScoreRange: Optional[RangeOfDecimal]
    videoViewabilityScoreRange: Optional[RangeOfDecimal]
    volumeControlPriority: Optional[VolumeControlPriority]
    weatherCondition: Optional[WeatherCondition]

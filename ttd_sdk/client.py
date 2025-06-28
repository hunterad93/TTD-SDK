import os
from typing import Optional, Dict, Any, Iterator, Literal
import requests

from .auth import TokenManager
from .logging import (
    configure_sdk_logging, 
    get_logger, 
    LogLevel,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL
)
from .exceptions import (
    TTDError,
    AuthenticationError,
    PermissionError,
    ResourceNotFoundError,
    ValidationError,
    RateLimitError,
    ServerError,
    ClientError,
)
from .resources.advertiser_resource import AdvertiserResource
from .resources.audience_resource import AudienceResource
from .resources.campaign_resource import CampaignResource
from .resources.creative_resource import CreativeResource
from .resources.data_group_resource import DataGroupResource
from .resources.first_party_element_resource import FirstPartyElementResource
from .resources.third_party_element_resource import ThirdPartyElementResource
from .resources.universal_pixel_resource import UniversalPixelResource
from .resources.ad_group_resource import AdGroupResource
from .resources.activity_log_resource import ActivityLogResource
from .resources.additional_fees_resource import AdditionalFeesResource
from .resources.bid_list_resource import BidListResource
from .resources.reports_resource import ReportsResource
from .resources.supply_vendor_resource import SupplyVendorResource
from .resources.ip_targeting_resource import IPTargetingResource

Method = Literal["GET", "POST"]

logger = get_logger(__name__)

class TTDClient:
    API_VERSION = "v3"
    
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        partner_id: Optional[str] = None,
        sandbox: bool = True,
        timeout: int = 240,
        max_retries: int = 3,
        log_level: Optional[LogLevel | int] = None,
        log_file: Optional[str] = None
    ):
        if log_level or log_file:
            configure_sdk_logging(
                level=log_level,
                log_file=log_file
            )
        
        self.username = username or os.getenv("TTD_USERNAME")
        self.password = password or os.getenv("TTD_PASSWORD")
        self.partner_id = partner_id or os.getenv("TTD_PARTNER_ID")
        
        if not self.username or not self.password:
            logger.error("Missing credentials")
            raise ValueError(
                "Credentials must be provided either directly or through environment variables "
                "(TTD_USERNAME and TTD_PASSWORD)"
            )
        
        if not self.partner_id:
            logger.error("Missing partner ID")
            raise ValueError(
                "Partner ID must be provided either directly or through environment variable "
                "(TTD_PARTNER_ID)"
            )
        
        logger.info("Initializing TTD client")
        logger.debug(f"Sandbox mode: {sandbox}")
        
        self.sandbox = sandbox
        self.timeout = timeout
        self.max_retries = max_retries
        
        self.token_manager = TokenManager(
            username=self.username,
            password=self.password,
            sandbox=self.sandbox
        )
        self.base_url = self.token_manager.base_url

        # Initialize all resources
        logger.debug("Initializing resources")
        self.advertisers = AdvertiserResource(self)
        self.audiences = AudienceResource(self)
        self.campaigns = CampaignResource(self)
        self.creatives = CreativeResource(self)
        self.data_groups = DataGroupResource(self)
        self.first_party_data = FirstPartyElementResource(self)
        self.third_party_data = ThirdPartyElementResource(self)
        self.universal_pixels = UniversalPixelResource(self)
        self.ad_groups = AdGroupResource(self)
        self.activity_logs = ActivityLogResource(self)
        self.additional_fees = AdditionalFeesResource(self)
        self.bid_lists = BidListResource(self)
        self.reports = ReportsResource(self)
        self.supply_vendors = SupplyVendorResource(self)
        self.ip_targeting = IPTargetingResource(self)

        self.session = requests.Session()
        retry_strategy = requests.adapters.Retry(
            total=max_retries,
            backoff_factor=61,  # This will make it wait 61 seconds between each retry
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE"],
            raise_on_status=False,
            respect_retry_after_header=False  # Ignore server's retry-after header
        )
        adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        logger.info("TTD client initialized successfully")

    def _get_headers(self) -> Dict[str, str]:
        token = self.token_manager.get_token()
        logger.debug(f"Using token for request: {token[:10]}...")
        return {
            "TTD-Auth": token,
            "Content-Type": "application/json"
        }

    def _handle_response(self, response: requests.Response) -> Dict:
        """Handle response and raise appropriate exceptions"""
        status_code = response.status_code
        
        if status_code < 400:
            return response.json()
        
        try:
            error_data = response.json()
        except ValueError:
            error_data = {}
        
        error_kwargs = {
            "message": str(response.reason),
            "status_code": status_code,
            "error_code": error_data.get('ErrorCode'),
            "request_id": response.headers.get('X-TTD-Request-ID'),
            "response_data": error_data,
            "response": response
        }
        
        if status_code == 429:
            raise RateLimitError(**error_kwargs)
        elif status_code >= 500:
            raise ServerError(**error_kwargs)
        elif status_code == 401:
            raise AuthenticationError(**error_kwargs)
        elif status_code == 403:
            raise PermissionError(**error_kwargs)
        elif status_code == 404:
            raise ResourceNotFoundError(**error_kwargs)
        else:
            raise ClientError(**error_kwargs)

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """Make HTTP request with retry handling"""
        url = f"{self.base_url}/{self.API_VERSION}/{endpoint.lstrip('/')}"
        
        kwargs["headers"] = self._get_headers()
        kwargs["timeout"] = self.timeout

        logger.debug(
            f"Making request: {method} {url}"
            f"\nParams: {kwargs.get('params')}"
            f"\nBody: {kwargs.get('json')}"
        )

        try:
            response = self.session.request(method, url, **kwargs)
            
            logger.debug(
                f"Response: {response.status_code} {response.reason}"
                f"\nResponse body: {response.json()}"
            )
            
            return self._handle_response(response)
                
        except requests.exceptions.RequestException as e:
            if e.response:
                return self._handle_response(e.response)
            raise ClientError(message=str(e))

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict:
        return self._make_request("GET", endpoint, params=params)
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict:
        return self._make_request("POST", endpoint, json=data)
        
    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict:
        return self._make_request("PUT", endpoint, json=data)
        
    def delete(self, endpoint: str) -> Dict:
        return self._make_request("DELETE", endpoint)

    def _paginate(
        self,
        method: Method,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        page_size: int = 1000,
        start_index: int = 0,
        exclude_total_counts: bool = True
    ) -> Iterator[Dict]:
        """
        Generic pagination handler for both GET and POST requests
        """
        total_results = 0
        current_page = 0
        
        logger.info(f"Starting pagination for {method} {endpoint}")
        
        params = {} if method == "POST" else (data or {})
        body = data if method == "POST" else None

        if body is not None:
            body["PageSize"] = page_size
            body["PageStartIndex"] = start_index
            body["ExcludeTotalCounts"] = exclude_total_counts
        else:
            params["PageSize"] = page_size
            params["PageStartIndex"] = start_index
            params["ExcludeTotalCounts"] = exclude_total_counts

        while True:
            current_page += 1
            logger.debug(f"Fetching page {current_page} (start_index: {start_index})")
            
            response = self._make_request(
                method=method,
                endpoint=endpoint,
                params=params if method == "GET" else None,
                json=body if method == "POST" else None
            )
            
            results = response.get("Result", [])
            result_count = response.get("ResultCount", 0)
            
            if not results or result_count == 0:
                break

            total_results += len(results)
            logger.info(f"Retrieved {len(results)} results (total so far: {total_results})")
            
            yield from results
            
            if result_count < page_size:
                break
            
            if body is not None:
                body["PageStartIndex"] += page_size
            else:
                params["PageStartIndex"] += page_size

        logger.info(f"Pagination complete. Total results: {total_results}")

    def get_with_pagination(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        page_size: int = 1000,
        exclude_total_counts: bool = True
    ) -> Iterator[Dict]:
        """
        Paginate through GET endpoint results
        """
        yield from self._paginate("GET", endpoint, params, page_size, exclude_total_counts=exclude_total_counts)

    def post_with_pagination(
        self,
        endpoint: str,
        data: Dict[str, Any],
        page_size: int = 1000,
        exclude_total_counts: bool = True
    ) -> Iterator[Dict]:
        """
        Paginate through POST endpoint results
        """
        yield from self._paginate("POST", endpoint, data, page_size, exclude_total_counts=exclude_total_counts)
import os
from typing import Optional, Dict, Any, Iterator, Literal
import requests

from .auth import TokenManager
from .utils.retry import RetryHandler
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
        timeout: int = 120,
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
        self.retry_handler = RetryHandler(max_retries=self.max_retries)

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
        logger.info("TTD client initialized successfully")

    def _get_headers(self) -> Dict[str, str]:
        token = self.token_manager.get_token()
        logger.debug(f"Using token for request: {token[:10]}...")
        return {
            "TTD-Auth": token,
            "Content-Type": "application/json"
        }

    def _handle_request_error(self, error: requests.exceptions.RequestException) -> None:
        if not error.response:
            logger.error(f"Request failed without response: {error}")
            raise ClientError(str(error))
            
        status_code = error.response.status_code
        try:
            error_data = error.response.json()
        except ValueError:
            error_data = {}
        
        request_id = error.response.headers.get('X-Request-ID')
        error_code = error_data.get('ErrorCode')
        message = error_data.get('Message', str(error))
        
        logger.error(f"Request failed: {status_code} - {message} (Request ID: {request_id})")
        
        error_kwargs = {
            "message": message,
            "status_code": status_code,
            "error_code": error_code,
            "request_id": request_id,
            "response_data": error_data,
            "response": error.response
        }
        
        if status_code == 401:
            raise AuthenticationError(**error_kwargs)
        elif status_code == 403:
            raise PermissionError(**error_kwargs)
        elif status_code == 404:
            raise ResourceNotFoundError(**error_kwargs)
        elif status_code == 429:
            raise RateLimitError(**error_kwargs)
        elif status_code >= 500:
            raise ServerError(**error_kwargs)
        else:
            raise ClientError(**error_kwargs)

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict:
        url = f"{self.base_url}/{self.API_VERSION}/{endpoint.lstrip('/')}"
        
        kwargs["headers"] = self._get_headers()
        kwargs["timeout"] = self.timeout

        logger.debug(f"Making {method} request to {endpoint}")

        def request_with_retry():
            try:
                response = requests.request(method, url, **kwargs)
                response.raise_for_status()
                
                data = response.json()
                logger.debug(f"Received response from {endpoint}: {str(data)[:100]}...")
                
                return data
            except requests.exceptions.RequestException as e:
                self._handle_request_error(e)

        return self.retry_handler.execute(request_with_retry)

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
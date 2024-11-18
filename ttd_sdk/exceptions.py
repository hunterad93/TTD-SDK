import logging
from typing import Optional, Dict, Any
from requests import Response

logger = logging.getLogger("ttd_sdk")

class TTDError(Exception):
    """Base exception for all TTD SDK errors"""
    def __init__(
        self, 
        message: str,
        status_code: Optional[int] = None,
        error_code: Optional[str] = None,
        request_id: Optional[str] = None,
        response_data: Optional[Dict[str, Any]] = None,
        response: Optional[Response] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.request_id = request_id
        self.response_data = response_data
        self.response = response
        
        logger.error(
            f"TTD API Error:\n"
            f"Message: {message}\n"
            f"Status Code: {status_code}\n"
            f"Error Code: {error_code}\n"
            f"Request ID: {request_id}\n"
            f"Response Data: {response_data}"
        )
        
        super().__init__(self.message)

class RateLimitError(TTDError):
    """Rate limit exceeded (429)"""
    @property
    def retry_after(self) -> float:
        """Get retry delay in seconds"""
        if not self.response:
            return 60.0
        
        # Try Retry-After header first
        retry_after = self.response.headers.get('Retry-After')
        if retry_after:
            try:
                return float(retry_after)
            except (ValueError, TypeError):
                pass

        # Try window size as fallback
        window_size = self.response.headers.get('window_size')
        if window_size:
            try:
                return float(window_size) / 1000  # Convert ms to seconds
            except (ValueError, TypeError):
                pass
        
        return 60.0  # Default fallback

    @property
    def rate_limit_info(self) -> Dict[str, Any]:
        """Get rate limit details for logging"""
        if not self.response:
            return {}
        
        return {
            'retry_after': self.retry_after,
            'window_size': self.response.headers.get('window_size'),
            'max_calls': self.response.headers.get('window_max_api_calls_allowed'),
            'window_start': self.response.headers.get('window_start_time_in_utc')
        }

# Other exception types
class AuthenticationError(TTDError): pass
class PermissionError(TTDError): pass
class ResourceNotFoundError(TTDError): pass
class ValidationError(TTDError): pass
class ServerError(TTDError): pass
class ClientError(TTDError): pass
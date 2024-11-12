import logging
from typing import Optional, Dict, Any
from requests import Response
from requests.exceptions import RequestException

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
        
        # Log error details
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
    def retry_after(self) -> Optional[float]:
        """Get the retry-after value from headers if available"""
        if not self.response:
            return None
        retry_after = self.response.headers.get('retry-after')
        return float(retry_after) if retry_after else None

# Keep other exceptions simple
class AuthenticationError(TTDError): pass
class PermissionError(TTDError): pass
class ResourceNotFoundError(TTDError): pass
class ValidationError(TTDError): pass
class ServerError(TTDError): pass
class ClientError(TTDError): pass
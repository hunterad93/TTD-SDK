from datetime import datetime, timedelta
from typing import Optional
import requests
import logging

logger = logging.getLogger(__name__)

class TokenManager:
    def __init__(self, username: str, password: str, sandbox: bool = False):
        self.username = username
        self.password = password
        self.base_url = (
            "https://ext-api.sb.thetradedesk.com" if sandbox 
            else "https://api.thetradedesk.com"
        )
        self._token: Optional[str] = None
        self._token_expiry: Optional[datetime] = None

    def get_token(self) -> str:
        if self._is_token_valid():
            logger.debug("Using existing valid token")
            return self._token

        logger.debug("Fetching new auth token")
        response = requests.post(
            f"{self.base_url}/v3/authentication",
            json={
                "Login": self.username,
                "Password": self.password,
                "TokenExpirationInMinutes": 1000
            }
        )
        response.raise_for_status()
        
        self._token = response.json()["Token"]
        self._token_expiry = datetime.now() + timedelta(minutes=900)
        logger.debug("New token generated, expires at: %s", self._token_expiry)
        return self._token

    def _is_token_valid(self) -> bool:
        if not self._token or not self._token_expiry:
            return False
        return datetime.now() < self._token_expiry 
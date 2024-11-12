import pytest
from unittest.mock import Mock
import requests
from ttd_sdk import TTDClient
from ttd_sdk.exceptions import AuthenticationError, RateLimitError

def test_client_init_with_direct_credentials(client):
    """Test client initialization with direct credentials"""
    assert client.username == "test_user"
    assert client.password == "test_pass"
    assert client.partner_id == "test_partner"
    assert client.sandbox is True

def test_client_init_with_env_vars(mock_auth, monkeypatch):
    """Test client initialization with environment variables"""
    monkeypatch.setenv("TTD_USERNAME", "env_user")
    monkeypatch.setenv("TTD_PASSWORD", "env_pass")
    monkeypatch.setenv("TTD_PARTNER_ID", "env_partner")
    
    client = TTDClient()
    assert client.username == "env_user"
    assert client.password == "env_pass"
    assert client.partner_id == "env_partner"

def test_client_missing_credentials(monkeypatch):
    """Test client initialization with missing credentials"""
    # Clear any existing env vars
    monkeypatch.delenv("TTD_USERNAME", raising=False)
    monkeypatch.delenv("TTD_PASSWORD", raising=False)
    monkeypatch.delenv("TTD_PARTNER_ID", raising=False)
    
    with pytest.raises(ValueError, match="Credentials must be provided"):
        TTDClient(partner_id="test")

def test_client_missing_partner_id(monkeypatch):
    """Test client initialization with missing partner ID"""
    # Clear any existing env vars
    monkeypatch.delenv("TTD_USERNAME", raising=False)
    monkeypatch.delenv("TTD_PASSWORD", raising=False)
    monkeypatch.delenv("TTD_PARTNER_ID", raising=False)
    
    with pytest.raises(ValueError, match="Partner ID must be provided"):
        TTDClient(username="test", password="test")

# Request Tests
def test_successful_get_request(mock_requests, client):
    """Test successful GET request"""
    mock_requests.return_value = Mock(
        status_code=200,
        json=Mock(return_value={"data": "test"}),
        raise_for_status=Mock()
    )
    
    response = client.get("test/endpoint", {"param": "value"})
    
    assert response == {"data": "test"}
    mock_requests.assert_called_with(
        "GET",
        f"{client.base_url}/test/endpoint",
        params={"param": "value"},
        headers=client._get_headers(),
        timeout=30
    )

def test_successful_post_request(mock_requests, client):
    """Test successful POST request"""
    mock_requests.return_value = Mock(
        status_code=200,
        json=Mock(return_value={"id": "123"}),
        raise_for_status=Mock()
    )
    
    response = client.post("test/endpoint", {"data": "test"})
    
    assert response == {"id": "123"}
    mock_requests.assert_called_with(
        "POST",
        f"{client.base_url}/test/endpoint",
        json={"data": "test"},
        headers=client._get_headers(),
        timeout=30
    )

def test_authentication_error(mock_requests, client):
    """Test handling of authentication errors"""
    error_response = Mock(
        status_code=401,
        json=Mock(return_value={"Message": "Invalid token"}),
        headers={"X-Request-ID": "123"},
        raise_for_status=Mock(
            side_effect=requests.exceptions.HTTPError(
                response=Mock(
                    status_code=401,
                    headers={"X-Request-ID": "123"},
                    json=Mock(return_value={"Message": "Invalid token"})
                )
            )
        )
    )
    mock_requests.return_value = error_response
    
    with pytest.raises(AuthenticationError) as exc_info:
        client.get("test/endpoint")
    
    assert exc_info.value.status_code == 401
    assert exc_info.value.request_id == "123"

def test_retry_on_rate_limit(mock_requests, client):
    """Test retry behavior on rate limit errors"""
    rate_limit_response = Mock(
        status_code=429,
        json=Mock(return_value={"Message": "Rate limit exceeded"}),
        headers={"retry-after": "2.0", "X-Request-ID": "123"},  # Add proper retry-after header
        raise_for_status=Mock(
            side_effect=requests.exceptions.HTTPError(
                response=Mock(
                    status_code=429,
                    headers={"retry-after": "2.0", "X-Request-ID": "123"},  # Add here too
                    json=Mock(return_value={"Message": "Rate limit exceeded"})
                )
            )
        )
    )
    success_response = Mock(
        status_code=200,
        json=Mock(return_value={"data": "success"}),
        raise_for_status=Mock(),
        headers={}
    )
    
    mock_requests.side_effect = [rate_limit_response, success_response]
    
    response = client.get("test/endpoint")
    
    assert response == {"data": "success"}
    assert mock_requests.call_count == 2
import pytest
from unittest.mock import Mock, patch
from ttd_sdk import TTDClient

def raise_for_real_request(*args, **kwargs):
    """Catch any non-mocked requests and raise an error"""
    url = kwargs.get("url", "") or (args[1] if len(args) > 1 else "")
    raise RuntimeError(
        f"REAL API CALL ATTEMPTED to {url}\n"
        "All requests must be mocked during testing!"
    )

@pytest.fixture(autouse=True)
def prevent_real_requests():
    """Global fixture to prevent any real HTTP requests"""
    with patch("requests.request", side_effect=raise_for_real_request), \
         patch("requests.post", side_effect=raise_for_real_request), \
         patch("requests.get", side_effect=raise_for_real_request):
        yield

@pytest.fixture
def mock_requests():
    """Mock for request calls"""
    with patch("requests.request") as mock:
        # Set up default success response
        mock.return_value = Mock(
            status_code=200,
            json=Mock(return_value={}),
            raise_for_status=Mock(),
            headers={}
        )
        yield mock

@pytest.fixture
def mock_auth():
    """Mock the auth token response"""
    with patch("requests.post") as mock:
        mock.return_value = Mock(
            status_code=200,
            json=lambda: {"Token": "fake-token"},
            raise_for_status=Mock()
        )
        yield mock

@pytest.fixture
def client(mock_auth):
    """Create a test client with mocked auth"""
    return TTDClient(
        username="test_user",
        password="test_pass",
        partner_id="test_partner",
        sandbox=True
    )
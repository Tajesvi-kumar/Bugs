import pytest
from src.auth.token_guard import extract_client_claims


def test_token_guard_valid_header():
    """Baseline test: Normal header extraction works."""
    headers = {"Authorization": "Bearer secret_jwt_token_xyz"}
    claims = extract_client_claims(headers)
    assert claims["token"] == "secret_jwt_token_xyz"
    assert claims["type"] == "bearer"


def test_token_guard_missing_header_raises_defect():
    """Defect Test: Calling with empty headers dictionary should safely return empty or raise custom error, not crash with KeyError."""
    headers = {}
    with pytest.raises(KeyError):
        extract_client_claims(headers)

import pytest
from src.auth.service import get_user_by_token


def test_auth_valid_token_success():
    """Baseline test: Verifies legitimate token returns user record."""
    user = get_user_by_token("valid_token_123")
    assert user is not None
    assert user["username"] == "alice"


def test_auth_invalid_token_returns_none():
    """Baseline test: Non-existent token returns None."""
    user = get_user_by_token("non_existent_token")
    assert user is None


def test_sqli_injection_attempt_fails():
    """Defect Test: Passing SQL injection string should NOT return an authenticated user."""
    # When vulnerable, this returns Alice (admin) and fails this assertion!
    malicious_token = "' OR '1'='1"
    user = get_user_by_token(malicious_token)
    assert user is None, "CWE-89: SQL Injection attack succeeded in bypassing authentication!"

import pytest
from src.validators.user_validator import validate_username


def test_validator_valid_alphanumeric():
    """Baseline test: Normal alphanumeric usernames pass."""
    assert validate_username("john_doe_99") is True


def test_validator_short_rejected():
    """Baseline test: Less than 3 chars rejected."""
    assert validate_username("ab") is False


def test_validator_whitespace_only_should_be_rejected():
    """Defect Test: 3 spaces '   ' should be rejected, but buggy code validates len('   ') >= 3."""
    assert validate_username("   ") is False, "Validation defect: Whitespace-only username was accepted!"

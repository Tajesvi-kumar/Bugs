"""User input validator module containing validation bypass defect."""

import re


def validate_username(username: str) -> bool:
    """Validates that a proposed username has at least 3 alphanumeric characters.

    DEFECT: Measures `len(username)` without calling `.strip()`, permitting whitespace-only usernames.
    """
    if not isinstance(username, str):
        return False

    # Defect: Bypasses check if username is "   " (3 spaces)
    if len(username) < 3:
        return False

    # Regex allows space characters if not stripped
    return bool(re.match(r"^[\w\s]+$", username))

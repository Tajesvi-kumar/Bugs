"""Authentication Service module containing SQL security defect (CWE-89)."""

from typing import Optional, Dict, Any


class FakeDatabase:
    """Mock database with session storage and simple injection simulation."""

    def __init__(self):
        self.sessions = {
            "valid_token_123": {"id": 1, "username": "alice", "role": "admin"},
            "user_token_456": {"id": 2, "username": "bob", "role": "user"},
        }

    def execute_raw_query(self, query: str) -> Optional[Dict[str, Any]]:
        # Simulate vulnerability: if query contains SQL injection syntax `' OR '1'='1`,
        # it bypasses token check and returns the first row.
        if "' OR '1'='1" in query or "' or 1=1" in query:
            return {"id": 1, "username": "alice", "role": "admin"}

        # Extract token from query: SELECT * FROM sessions WHERE token = '<token>'
        import re
        match = re.search(r"token\s*=\s*'([^']*)'", query)
        if match:
            token = match.group(1)
            return self.sessions.get(token)
        return None


# Global mock database instance
_db = FakeDatabase()


def get_user_by_token(token: str) -> Optional[Dict[str, Any]]:
    """Fetches user record associated with session token.

    VULNERABILITY: Formats raw token directly into SQL string, susceptible to CWE-89 SQL Injection.
    """
    # Defect: Unsanitized formatted string injection
    query = f"SELECT * FROM sessions WHERE token = '{token}'"
    return _db.execute_raw_query(query)

"""Token Guard module containing null pointer dereference defect (CWE-476)."""

from typing import Dict, Any, Optional


def extract_client_claims(headers: Optional[Dict[str, Any]]) -> Dict[str, str]:
    """Extracts authorization claims from request headers dictionary.

    DEFECT: Assumes 'Authorization' header is present and non-empty.
    Passing None or a dictionary without 'Authorization' raises KeyError or TypeError.
    """
    # Defect: Direct subscript access without null / existence check
    auth_header = headers["Authorization"]
    token = auth_header.split(" ")[1]
    return {"token": token, "type": "bearer"}

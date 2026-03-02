"""JWT-based authentication for FL node registration."""
from __future__ import annotations

import hashlib
import hmac
import json
import time
import base64


class JWTValidator:
    """Minimal JWT validator for node authentication."""

    def __init__(self, secret: str) -> None:
        self._secret = secret.encode()

    def create_token(self, node_id: str, ttl: int = 3600) -> str:
        """Create a signed JWT for a node."""
        header = base64.urlsafe_b64encode(json.dumps({"alg": "HS256"}).encode()).decode()
        payload = base64.urlsafe_b64encode(json.dumps({
            "sub": node_id,
            "exp": int(time.time()) + ttl,
        }).encode()).decode()
        sig = hmac.new(self._secret, f"{header}.{payload}".encode(), hashlib.sha256)
        return f"{header}.{payload}.{base64.urlsafe_b64encode(sig.digest()).decode()}"

    def validate_token(self, token: str) -> dict | None:
        """Validate token signature and expiry. Returns payload or None."""
        parts = token.split(".")
        if len(parts) != 3:
            return None
        header, payload, sig = parts
        expected = hmac.new(self._secret, f"{header}.{payload}".encode(), hashlib.sha256)
        expected_sig = base64.urlsafe_b64encode(expected.digest()).decode()
        if not hmac.compare_digest(sig, expected_sig):
            return None
        data = json.loads(base64.urlsafe_b64decode(payload))
        if data.get("exp", 0) < time.time():
            return None
        return data

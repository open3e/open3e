"""Simple password hashing/verification using hashlib.scrypt."""

from __future__ import annotations

import hashlib
import os
import secrets
import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse
from fastapi import Request

SESSION_TIMEOUT = 86400  # 24 hours


def hash_password(password: str) -> str:
    """Hash *password* with scrypt. Returns 'salt_hex:hash_hex'."""
    salt = os.urandom(16)
    hashed = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=16384,
        r=8,
        p=1,
        dklen=32,
    )
    return f"{salt.hex()}:{hashed.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    """Verify *password* against a stored 'salt_hex:hash_hex' string."""
    try:
        salt_hex, hash_hex = stored_hash.split(":", 1)
    except ValueError:
        return False
    salt = bytes.fromhex(salt_hex)
    expected = bytes.fromhex(hash_hex)
    actual = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=16384,
        r=8,
        p=1,
        dklen=32,
    )
    return actual == expected


class SessionManager:
    """In-memory session store with expiry."""

    def __init__(self):
        self._sessions: dict[str, float] = {}  # token -> last_access

    def create_session(self) -> str:
        token = secrets.token_hex(32)
        self._sessions[token] = time.time()
        return token

    def validate_session(self, token: str) -> bool:
        if token not in self._sessions:
            return False
        last_access = self._sessions[token]
        if time.time() - last_access > SESSION_TIMEOUT:
            del self._sessions[token]
            return False
        self._sessions[token] = time.time()  # refresh
        return True

    def destroy_session(self, token: str) -> None:
        self._sessions.pop(token, None)

    def cleanup_expired(self) -> None:
        now = time.time()
        expired = [t for t, ts in self._sessions.items() if now - ts > SESSION_TIMEOUT]
        for t in expired:
            del self._sessions[t]


class AuthMiddleware(BaseHTTPMiddleware):
    """Optional password protection middleware."""

    def __init__(self, app, store, session_manager: SessionManager):
        super().__init__(app)
        self.store = store
        self.sessions = session_manager
        self._auth_enabled = None
        self._cache_time = 0

    async def dispatch(self, request: Request, call_next):
        # Re-read auth state from DB every 5 seconds
        now = time.time()
        if self._auth_enabled is None or (now - self._cache_time) > 5:
            enabled = (await self.store.get_setting("auth_enabled")) == "1"
            has_password = bool(await self.store.get_setting("auth_password_hash"))
            # Only enforce auth if BOTH enabled AND a password is set
            self._auth_enabled = enabled and has_password
            self._cache_time = now

        if not self._auth_enabled:
            return await call_next(request)

        # Allow public paths
        path = request.url.path
        if path in ("/login", "/logout", "/api/auth/logout") or path.startswith("/static"):
            return await call_next(request)

        # Check session cookie
        token = request.cookies.get("open3e_session")
        if token and self.sessions.validate_session(token):
            return await call_next(request)

        # Not authenticated — redirect to login (for pages) or 401 (for API)
        if path.startswith("/api/"):
            from starlette.responses import JSONResponse
            return JSONResponse({"detail": "Authentication required"}, status_code=401)
        return RedirectResponse("/login", status_code=302)

    def invalidate_cache(self):
        """Call when auth settings change."""
        self._auth_enabled = None

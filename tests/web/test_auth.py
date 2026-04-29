import time
import pytest
from unittest.mock import patch
from open3e.web.auth import hash_password, verify_password, SessionManager


class TestPasswordHashing:
    def test_hash_and_verify(self):
        hashed = hash_password("mypassword")
        assert verify_password("mypassword", hashed)

    def test_wrong_password(self):
        hashed = hash_password("correct")
        assert not verify_password("wrong", hashed)

    def test_different_hashes(self):
        h1 = hash_password("same")
        h2 = hash_password("same")
        assert h1 != h2  # different salts


class TestSessionManager:
    def test_create_and_validate(self):
        sm = SessionManager()
        token = sm.create_session()
        assert sm.validate_session(token)

    def test_invalid_token(self):
        sm = SessionManager()
        assert not sm.validate_session("nonexistent")

    def test_destroy_session(self):
        sm = SessionManager()
        token = sm.create_session()
        sm.destroy_session(token)
        assert not sm.validate_session(token)

    @patch("open3e.web.auth.time")
    def test_expired_session(self, mock_time):
        sm = SessionManager()
        mock_time.time.return_value = 1000.0
        token = sm.create_session()
        # Jump forward past timeout
        mock_time.time.return_value = 1000.0 + 86401
        assert not sm.validate_session(token)

    def test_cleanup_expired(self):
        sm = SessionManager()
        token = sm.create_session()
        # Manually expire it
        sm._sessions[token] = 0  # epoch = very old
        sm.cleanup_expired()
        assert not sm.validate_session(token)

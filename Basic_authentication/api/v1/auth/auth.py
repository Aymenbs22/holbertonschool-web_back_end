#!/usr/bin/env python3
"""create a class to manage the API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Vlass"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method def require_auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """public method def authorization_header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method def current_user"""
        return None

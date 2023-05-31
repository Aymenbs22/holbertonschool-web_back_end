#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.auth.basic_auth import BasicAuth
from api.v1.app import auth


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth.
    For the moment this class will be empty"""

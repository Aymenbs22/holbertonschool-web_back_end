#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """class SessionAuth that inherits from Auth"""
    def __init__(self):
        return

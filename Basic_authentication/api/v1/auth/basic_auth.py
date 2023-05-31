#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth.
    For the moment this class will be empty"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        afterbas = authorization_header.split(" ")[1]
        return afterbas

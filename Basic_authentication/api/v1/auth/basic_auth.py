#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.auth.auth import Auth
import base64
import binascii


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth.
    For the moment this class will be empty"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """method in the class BasicAuth that returns the Base64
        part of the Authorization header for a Basic Authentication"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        afterbas = authorization_header.split(" ")[1]
        return afterbas

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """method in the class BasicAuth that returns the decoded
        value of a Base64 string base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            b64decode = base64.b64decode(base64_authorization_header)
        except Exception:
            return
        utf8 = b64decode.decode('utf-8')
        return utf8

#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """class SessionAuth that inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """instance method that creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        SessionID = str(uuid.uuid4())
        self.user_id_by_session_id[SessionID] = user_id
        return SessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """instance method that returns a
        User ID based on a Session ID"""
        if session_id is None:
            return None
        if type(session_id) != str:
            return None
        userid = self.user_id_by_session_id.get(session_id)
        return userid
#!/usr/bin/env python3
"""method that takes in a password
string arguments and returns bytes"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """method that takes in a password
    string arguments and returns bytes"""
    mySalt = bcrypt.gensalt()
    bytePwd = bcrypt.hashpw(password.encode('utf-8'), mySalt)
    return bytePwd


def _generate_uuid() -> str:
    """function should return a string representation
    of a new UUID. Use the uuid module"""
    id = uuid.uuid4()
    strid = str(id)
    return strid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """save the user to the database
          and return the User object"""
        try:
            if self._db.find_user_by(email=email):
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashedpass = _hash_password(password)
            user = self._db.add_user(email, hashedpass)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """locating the user by email. If it exists, check the
        password with bcrypt.checkpw. If it matches return True.
        In any other case, return False"""
        try:
            user = self._db.find_user_by(email=email)
            encodedpass = password.encode('utf-8')
            pw_check = bcrypt.checkpw(encodedpass, user.hashed_password)
            return True and pw_check
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """method should find the user corresponding to the email,
        generate a new UUID and store it in the database as
        the user’s session_id, then return the session ID"""
        try:
            user = self._db.find_user_by(email=email)
            uuid = _generate_uuid()
            self._db.update_user(user.id, session_id=uuid)
            return uuid
        except Exception:
            return

    def get_user_from_session_id(self, session_id: str) -> User:
        """If the session ID is None or no user is found,
        return None. Otherwise return the corresponding user."""
        if not session_id:
            return None
        else:
            user = self._db.find_user_by(session_id=session_id)
            return user

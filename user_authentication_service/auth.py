#!/usr/bin/env python3
"""method that takes in a password
string arguments and returns bytes"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """method that takes in a password
    string arguments and returns bytes"""
    mySalt = bcrypt.gensalt()
    bytePwd = bcrypt.hashpw(password.encode('utf-8'), mySalt)
    return bytePwd


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

#!/usr/bin/env python3
"""method that takes in a password
string arguments and returns bytes"""

import bcrypt


def _hash_password(password: str) -> str:
    """method that takes in a password
    string arguments and returns bytes"""
    mySalt = bcrypt.gensalt()
    bytePwd = bcrypt.hashpw(password.encode('utf-8'), mySalt)
    return bytePwd

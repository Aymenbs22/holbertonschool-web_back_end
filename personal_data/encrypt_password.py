#!/usr/bin/env python3
"""Implement a hash_password function that expects
one string argument name password and returns a salted,
hashed password, which is a byte string"""


import bcrypt


def hash_password(password: str) -> bytes:
    password = password.encode('utf-8')
    mySalt = bcrypt.gensalt()
    pwd_hash = bcrypt.hashpw(password, mySalt)
    return (pwd_hash)

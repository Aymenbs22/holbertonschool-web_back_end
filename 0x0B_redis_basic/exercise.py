#!/usr/bin/env python3
"""strings to Redis"""
import redis
from typing import Union
import uuid


class Cache():
    """Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes a data argument and returns a string
        generate a random key (e.g. using uuid) store the input data in
        Redis using the random key and return the key"""
        uuid1 = str(uuid.uuid1())
        self._redis.set(uuid1, data)
        return uuid1

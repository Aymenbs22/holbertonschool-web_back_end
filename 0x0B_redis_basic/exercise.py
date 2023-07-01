#!/usr/bin/env python3
"""strings to Redis"""
import redis
from typing import Union, Optional, Callable
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

    def get(self, key: str, fn: Optional[Callable] = None) -> str:
        """create a get method that take a key string argument and
        an optional Callable argument named fn. This callable will
        be used to convert the data back to the desired format"""
        value = self._redis.get(key)
        return value

    def get_str(self) -> str:
        """get_str"""
        return

    def get_int(self) -> int:
        """get_int"""
        return

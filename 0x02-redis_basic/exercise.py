#!/usr/bin/env python3
"""Module to utilize the Redis database, a NoSQL data storage system
"""
import uuid
import redis
from typing import Union, Callable


class Cache:
    """Object for storing data in a Redis data storage."""
    def __init__(self) -> None:
        """Initializes a Cache instance."""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in a Redis data storage and returns the key."""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Get value from a Redis data storage."""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Get a string value from a Redis data storage."""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Get an integer value from a Redis data storage."""
        return self.get(key, lambda x: int(x))


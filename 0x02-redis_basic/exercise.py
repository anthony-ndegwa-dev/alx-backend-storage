#!/usr/bin/env python3
"""Module to utilize the Redis database, a NoSQL data storage system
"""
import uuid
import redis
from typing import Union


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


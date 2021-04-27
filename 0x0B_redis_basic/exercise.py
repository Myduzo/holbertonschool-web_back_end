#!/usr/bin/env python3
""" Redis exercice file
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Counts how many times methods of
    the Cache class are called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Function decorator """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Stores the history of inputs and outputs
    for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Function decorator """
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))

        output = str(method(self, *args, **kwds))
        self._redis.rpush(method.__qualname__ + ':outputs', output)

        return output
    return wrapper


def replay(fn: Callable):
    qual = fn.__qualname__
    print({} + 'was called' + {} + 'times:'.format(qual, count_calls))


class Cache():
    """ Class for adding Cache
    """
    def __init__(self):
        """ Initialisation of variables
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Writing strings to Redis
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get_str(self, key: str) -> str:
        """ Parameterizes a value from byte str to str
        """
        return self._redis.get(key)

    def get_int(self, key: str) -> int:
        """ Parameterizes a value from byte str to int
        """
        return self._redis.get(key)

    def get(self, key: str, fn: Optional[Callable] = None):
        """ Reading from Redis and recovering original type
        """
        val = self._redis.get(key)
        return val if not fn else fn(val)

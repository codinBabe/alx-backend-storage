#!/usr/bin/env python3
"""A simple implementation of a Redis cache."""

import redis
import uuid
from typing import Callable, Any, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """returns a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for decorated function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for the decorated function"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


def replay(fn: Callable) -> None:
    """Display the history of calls of a particular function."""
    red = redis.Redis()
    func_name = fn.__qualname__
    val = red.get(func_name)
    try:
        val = int(val.decode('utf-8'))
    except Exception:
        val = 0
    print("{} was called {} times:".format(func_name, val))
    inputs = red.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = red.lrange("{}:outputs".format(func_name), 0, -1)

    for input_val, output_val in zip(inputs, outputs):
        try:
            input_val = input_val.decode('utf-8')
        except Exception:
            input_val = ""
        try:
            output_val = output_val.decode('utf-8')
        except Exception:
            output_val = ""
        print("{}(*{}) -> {}".format(func_name, input_val, output_val))


class Cache:
    """A simple implementation of a Redis cache."""
    def __init__(self) -> None:
        """Initialize the Cache object."""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, float, int]) -> str:
        """Store the input data in Redis and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, float, int]:
        """Retrieve the data from Redis and apply the
        conversion function if provided."""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Retrieve the data from Redis and convert it to a string."""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve the data from Redis and convert it to an integer."""
        return self.get(key, lambda d: int(d))

#!/usr/bin/env python3
"""A simple implementation of a Redis cache."""


import redis
import requests
from functools import wraps
from typing import Callable


red = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """Returns a Callable that caches the output of a function."""
    @wraps(method)
    def wrapper(url) -> str:
        """Returns a string."""
        red.incr(f'count:{url}')
        result = red.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        red.set(f'count:{url}', 0)
        red.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@data_cacher
def get_page(url: str) -> str:
    """Returns the HTML content of a page."""
    return requests.get(url).text

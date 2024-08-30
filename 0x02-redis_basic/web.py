#!/usr/bin/env python3
"""A simple implementation of a Redis cache."""


import redis
import requests
from functools import wraps


red = redis.Redis()


def url_count(method):
    """decorator for get_page function"""
    @wraps(method)
    def wrapper(url):
        """wrapper for get_page function"""
        key = "cached:" + url
        cached_value = red.get(key)
        if cached_value:
            return cached_value.decode("utf-8")

            # key for counting the number of times a URL was accessed
        key_count = "count:" + url
        html_content = method(url)

        red.incr(key_count)
        red.set(key, html_content, ex=10)
        red.expire(key, 10)
        return html_content
    return wrapper


@url_count
def get_page(url: str) -> str:
    """returns the content of a URL"""
    results = requests.get(url)
    return results.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')

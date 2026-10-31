# Implement a decorator that caches the return vales of a function, so that when it called wiht the same arguments the cavched value is returned instead of re-executing the function.

import time


def cache_result(func):
    cache = {}
    print(cache)

    def wrapper(*args, **kwargs):
        # frozenset is used to create an immutable set of the keyword arguments, which can be used as a key in the cache dictionary.
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print(f"Returning cached result for {func.__name__} with arguments {args} and keyword arguments {kwargs}")
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            print(f"Caching result for {func.__name__} with arguments {args} and keyword arguments {kwargs}")
            return result

    return wrapper


@cache_result
def long_running_function(n):
    time.sleep(n)
    return n * 2

print(long_running_function(3))  # This will take 3 seconds and return 6
print(long_running_function(3))  # This will return 6 immediately from cache
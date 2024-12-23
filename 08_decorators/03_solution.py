# 3. Implement a decorator that caches the return values of a function, 
# so that when it's called with the same arguments, 
# the cached value is returned instead of re-executing the function.

import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        print("cache_value" , cache_value)
        return result
    return wrapper

@cache
def running_function(a,b):
    time.sleep(4)
    return a+b

print(running_function(2,3))
print(running_function(4,3))
print(running_function(2,3))


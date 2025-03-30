from functools import wraps
import time

# 1.Decorator to allow only admin users to call the function
def is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('user_type') != 'admin':
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return wrapper
@is_admin
def show_customer_receipt(user_type: str):
    print("Access granted. Showing receipt...")


# 2.Decorator to catch and print errors
def catch_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found an error during execution: {type(e).__name__} - {e}")
    return wrapper
@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


# 4.Decorator for caching function results
def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@cache_results
def slow_function(n):
    time.sleep(2)
    return n * n
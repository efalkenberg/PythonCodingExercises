import time
import random


def retry(attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@retry(5)
def say_hello(name):
    print(f"Hello {name}")


say_hello("World")

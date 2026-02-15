import time
from functools import wraps


def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        try:
            return fn(*args, **kwargs)
        finally:
            t1 = time.time()
            print(f"{fn.__name__} took {t1 - t0:.4f} seconds")

    return wrapper


@timed
def slow_function():
    time.sleep(1.5)
    return "Done"


slow_function()

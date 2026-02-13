from functools import lru_cache, wraps
import time


def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = fn(*args, **kwargs)
        t1 = time.time()
        print(f"{fn.__name__} {args} took {t1-t0:.4f} seconds")
        return result

    return wrapper


@lru_cache(maxsize=128)
@timed
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(10))  # 55
    print(fib(50))  # 12586269025
    print(fib(50))  # 12586269025

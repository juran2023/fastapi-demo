from contextlib import contextmanager
import time


@contextmanager
def managed(name: str):
    t0 = time.time()
    print("enter", name)
    try:
        yield
    finally:
        t1 = time.time()
        print(f"exit {name} elapsed: {t1 - t0:.4f} seconds")


with managed("demo"):
    print("work")
    time.sleep(1.5)

"""
并发选型对比：thread / process / async
- IO 场景：sleep 模拟网络请求，对比线程池 vs async
- CPU 场景：大循环计算，对比线程池 vs 进程池（看 GIL 影响）
"""

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


TASKS = 8
CPU_N = 10_000_000


def IO_TASK(n: int) -> int:
    time.sleep(1)
    return n


async def ASYNC_IO_TASK(n: int) -> int:
    await asyncio.sleep(1)
    return n


def CPU_TASK(n: int) -> int:
    x = 0
    for i in range(CPU_N):
        x = i**2
    return n, x


async def doAsyncTask():
    t0 = time.time()

    await asyncio.gather(*map(ASYNC_IO_TASK, range(TASKS)))
    t1 = time.time()

    print(f"async task took {t1-t0:.4f} seconds")


def doThreadPoolTask():
    t0 = time.time()
    with ThreadPoolExecutor() as pool:
        list(pool.map(IO_TASK, range(TASKS)))
    t1 = time.time()
    print(f"doTheadPoolTask took {t1-t0:.4f} seconds")


def doCPUThreadPoolTask():
    t0 = time.time()
    with ThreadPoolExecutor() as pool:
        list(pool.map(CPU_TASK, range(TASKS)))
    t1 = time.time()
    print(f"doCPUThreadPoolTask took {t1-t0:.4f} seconds")


def doCPUProcessPoolTask():
    t0 = time.time()
    with ProcessPoolExecutor() as pool:
        list(pool.map(CPU_TASK, range(TASKS)))
    t1 = time.time()
    print(f"doCPUProcessPoolTask took {t1-t0:.4f} seconds")


def main():
    asyncio.run(doAsyncTask())
    doThreadPoolTask()
    doCPUProcessPoolTask()
    doCPUThreadPoolTask()


if __name__ == "__main__":
    main()

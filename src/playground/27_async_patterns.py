"""
27 - Async Patterns: 并发请求 10 个 URL
- asyncio.gather 并发
- asyncio.Semaphore 限制并发为 3
"""

import asyncio
import time

import aiohttp

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]


# ---------- 1. asyncio.gather 并发请求 ----------
async def fetch(session: aiohttp.ClientSession, url: str, idx: int) -> str:
    """请求单个 URL，返回状态码和耗时。"""
    start = time.perf_counter()
    async with session.get(url) as resp:
        await resp.read()
        elapsed = time.perf_counter() - start
        result = f"[gather]  #{idx:>2d}  status={resp.status}  {elapsed:.2f}s"
        print(result)
        return result


async def gather_demo():
    print("=== asyncio.gather：10 个请求全部并发 ===")
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, i) for i, url in enumerate(URLS)]
        results = await asyncio.gather(*tasks)
    total = time.perf_counter() - start
    print(f"--- gather 总耗时: {total:.2f}s  (理论 ~1s) ---\n")
    return results


# ---------- 2. Semaphore 限制并发为 3 ----------
sem = asyncio.Semaphore(3)


async def fetch_with_sem(session: aiohttp.ClientSession, url: str, idx: int) -> str:
    """在 semaphore 保护下请求，最多同时 3 个。"""
    async with sem:  # 超过 3 个协程会在此等待
        start = time.perf_counter()
        async with session.get(url) as resp:
            await resp.read()
            elapsed = time.perf_counter() - start
            result = f"[sem=3]   #{idx:>2d}  status={resp.status}  {elapsed:.2f}s"
            print(result)
            return result


async def semaphore_demo():
    print("=== Semaphore(3)：最多同时 3 个请求 ===")
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_sem(session, url, i) for i, url in enumerate(URLS)]
        results = await asyncio.gather(*tasks)
    total = time.perf_counter() - start
    print(f"--- semaphore 总耗时: {total:.2f}s  (理论 ~4s, ceil(10/3)*1) ---\n")
    return results


# ---------- main ----------
async def main():
    await gather_demo()
    await semaphore_demo()


if __name__ == "__main__":
    asyncio.run(main())

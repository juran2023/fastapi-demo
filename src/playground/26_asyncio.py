import asyncio
import time


async def main():
    await asyncio.gather(
        asyncio.sleep(1),
        asyncio.sleep(1),
        asyncio.sleep(1),
    )


t0 = time.time()
asyncio.run(main())
t1 = time.time()
print(f"main() took {t1- t0:.4f} seconds")

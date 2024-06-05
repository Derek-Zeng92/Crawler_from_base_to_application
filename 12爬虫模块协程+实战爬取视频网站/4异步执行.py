import time
import asyncio


async def run(i):
    print("lucky is a good man", i)
    # 模拟一个耗时IO
    await asyncio.sleep(2)
    print("lucky is a nice man", i)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = []
    t1 = time.time()

    for url in range(1, 5):
        coroutine = run(url)
        task = asyncio.ensure_future(coroutine)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    t2 = time.time()
    print("总耗时：%.2f" % (t2 - t1))
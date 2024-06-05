import asyncio


async def run():
    print('开始异步')
    await asyncio.sleep(2)
    print('结束异步')


if __name__ == '__main__':
    con = run()
    # 创建task
    task = asyncio.ensure_future(con)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)


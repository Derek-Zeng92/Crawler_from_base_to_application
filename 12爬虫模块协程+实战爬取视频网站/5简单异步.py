import asyncio


async def run():
    print('run函数开始')
    #  这个位置的asyncio.sleep()  用于携程对象中的阻塞等待
    await asyncio.sleep(2)
    print('run函数结束')


if __name__ == '__main__':
    con = run()
    asyncio.run(con)

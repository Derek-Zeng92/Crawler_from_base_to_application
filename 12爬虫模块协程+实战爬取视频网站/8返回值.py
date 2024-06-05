import asyncio


async def run(url):
    print('接受地址：',url)
    await asyncio.sleep(2)
    print('结束异步')
    return url

# 回调函数
def call_back(future):
    print(future)
    print('回调函数接收返回值', future.result())

if __name__ == '__main__':
    con = run('百度')
    # 创建任务
    task = asyncio.ensure_future(con)
    print('task', task)
    # 添加回调操作 获取返回值
    task.add_done_callback(call_back)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)

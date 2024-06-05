import asyncio

# 异步任务
async def run(url):
    print('协程', url, '开始抓取')
    return url

# 回调函数
def call_back(f):
    print('返回值', f.result())

async def main():
    url_list = ['baidu.com', 'taobao.com', 'aiqiyi.com']
    tasks = []
    for url in url_list:
        con = run(url)
        task = loop.create_task(con)
        task.add_done_callback(call_back)
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
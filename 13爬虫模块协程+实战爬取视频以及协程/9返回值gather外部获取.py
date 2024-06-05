import asyncio

# 异步任务
async def run(url):
    print('协程', url, '开始抓取')
    return url


async def main():
    url_list = ['baidu.com', 'taobao.com', 'aiqiyi.com']
    tasks = []
    for url in url_list:
        con = run(url)
        task = asyncio.create_task(con)
        tasks.append(task)
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    done = loop.run_until_complete(main())
    for f in done:
        print('获取返回值', f)

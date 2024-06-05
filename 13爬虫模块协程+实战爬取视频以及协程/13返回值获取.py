import aiohttp
import json
import asyncio

async def fetch(session, url):
    # 异步请求网址
    async with session.post(url, data='传递数据') as response:
        # 将相应内容进行返回
        # return await response.text()
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        source = await fetch(session, 'http://httpbin.org/post')
        # print(json.loads(source))
        print(source)


asyncio.run(main())







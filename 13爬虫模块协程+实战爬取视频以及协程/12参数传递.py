import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        params = {'name': 'lucky', 'age': 18}
        async with session.get('http://httpbin.org/get', params=params) as response:
            # 将相应内容进行返回
            print(response.url)  # 获取当前请求的url
            return await response.text()

asyncio.run(main())







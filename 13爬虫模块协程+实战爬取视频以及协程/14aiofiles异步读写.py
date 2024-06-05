import asyncio
import aiofiles


async def main():
    async with aiofiles.open('1多任务ensure_future.py', encoding='UTF-8') as f:
        return await f.readlines()




print(asyncio.run(main()))
'''
测试ip是否可用的文件
'''
import asyncio
import time

import aiohttp
from proxy_redis import ProxyRedis


async def test_ip(ip, p_r, sem):
    try:
        # 信号量并发控制
        async with sem:
            async with aiohttp.ClientSession() as session:
                async with session.get('http://httpbin.org/ip', proxy='http://'+ip, timeout=10) as resp:
                    con = await resp.text()  # 获取数据
                    if con:
                        # 设置最大权重
                        p_r.zset_zadd(ip)
                        # print('正常IP：',ip)
                    else:
                        # 降低权重
                        p_r.zset_zincrby(ip)
    except Exception as e:
        # print('错误ip：',ip, e)
        # 降低权重
        p_r.zset_zincrby(ip)

async def main():
    # 实例化处理ip的类
    p_r = ProxyRedis()
    ip_list = p_r.zset_zrange()  # 获取所有ip
    sem = asyncio.Semaphore(100)  # 并发控制
    if ip_list:
        tasks = []  # 存放所有的任务
        for ip in ip_list:
            # 添加任务
            tasks.append(asyncio.create_task(test_ip(ip, p_r, sem)))
        await asyncio.wait(tasks)

def run():
    count=0
    while True:
        count+=1
        try:
            asyncio.run(main())
            time.sleep(15)
        except Exception as e:
            print('ip测试异步出现错误', e)

if __name__ == '__main__':
    # asyncio.run(main())
    run()
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import time

# def run():
def run(i):
    print('开启线程', i)
    time.sleep(5)
    print('结束线程', i)
    return i

# 开启线程池  并发5个线程
pool = ThreadPoolExecutor(5)

# 列表推导式 等同于上方
# tasks = [pool.submit(run, i) for i in range(5)]

# 获取返回值
# for val in as_completed(tasks):
    # 获取值
    # print(val.result())


for val in pool.map(run, list(range(5))):
    print(val)
from concurrent.futures import ThreadPoolExecutor, wait
import time

# def run():
def run(i):
    print('开启线程', i)
    time.sleep(5)
    print('结束线程', i)

# 开启线程池  并发5个线程
pool = ThreadPoolExecutor(5)
# 如何放入线程池
# for i in range(5):
    # 传参 正常放入就可以
    # pool.submit(run, i)
# 列表推导式 等同于上方
# tasks = [pool.submit(run, i) for i in range(5)]
# wait(tasks)  # 等待 子线程执行
# print('over')
# print(tasks)

pool.map(run, list(range(5)))

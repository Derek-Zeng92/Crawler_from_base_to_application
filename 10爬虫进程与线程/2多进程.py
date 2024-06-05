import time
from multiprocessing import Process

def run1():
    for i in range(5):
        print('我是run1函数')
        # 当前代码阻塞在这了  卡在这了
        time.sleep(1)

def run2():
    for i in range(5):
        print('我是run2函数')
        # 当前代码阻塞在这了  卡在这了
        time.sleep(1)

if __name__ == '__main__':
    t1 = time.time()
    p1 = Process(target=run1)  # 创建子进程p1
    p2 = Process(target=run2)  # 创建子进程p2
    p1.start()  # 开启p1子进程
    p2.start()  # 开启p2子进程
    p1.join()  # 阻塞等待 p1子进程执行完  主进程在等待子进程干活啊
    p2.join()  # 阻塞等待 p2 子进程执行完
    print('我是下面的代码')
    print(time.time() - t1)
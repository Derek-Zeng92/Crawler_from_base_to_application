from multiprocessing import Process, Queue


def run(que):
    # 将数据放进队列中
    print('子进程放数据')
    que.put(1)
    que.put(2)
    que.put(3)


if __name__ == '__main__':
    # 创建队列对象
    que = Queue()
    p = Process(target=run, args=(que, ))
    p.start()
    p.join()
    print('主进程获取数据', que.get())
    print('主进程获取数据', que.get())
    print('主进程获取数据', que.get())
    # 如果队列中没有数据了  会阻塞等待
    # print('主进程获取数据', que.get())
    # 如果在timeout时间内 还没有数据 跑出异常
    # print('主进程获取数据', que.get(timeout=3))

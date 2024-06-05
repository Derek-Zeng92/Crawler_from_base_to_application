from multiprocessing import Process, Queue, Manager


def run(List):
    # 将数据放进队列中
    print('子进程放数据')
    List.append('lucky')
    List.append(18)

if __name__ == '__main__':
    # 创建队列对象
    List = Manager().list()
    p = Process(target=run, args=(List, ))
    p.start()
    p.join()
    print('主进程获取数据', List)
    # 自己回去练习
    # 子进程之间是否可以通信
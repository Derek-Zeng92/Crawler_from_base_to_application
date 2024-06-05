from multiprocessing import Process, Queue, Manager


def run(Dict):
    # 将数据放进队列中
    print('子进程放数据')
    Dict['name'] = 'lucky'
    Dict['age'] = '18'


if __name__ == '__main__':
    # 创建队列对象
    Dict = Manager().dict()
    p = Process(target=run, args=(Dict, ))
    p.start()
    p.join()
    print('主进程获取数据', Dict)

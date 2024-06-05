import time
from multiprocessing import Process

num = 1
def run1():
    # 声明num为全局变量
    global num
    num = 2  # 更改全局变量num的值为2
    print('我是run1函数', num)


if __name__ == '__main__':
    Process(target=run1).start()
    print('over')
    print(num)  # 1  进程间是独立的  每个进程有自己的独立存储

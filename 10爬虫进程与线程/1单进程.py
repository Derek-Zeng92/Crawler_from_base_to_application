import time


def run1():
    print('我是run函数')
    # 当前代码阻塞在这了  卡在这了
    time.sleep(1000)


def run2():
    print('我是run函数')
    # 当前代码阻塞在这了  卡在这了
    time.sleep(1000)
run1()
run2()
print('我是下面的代码')
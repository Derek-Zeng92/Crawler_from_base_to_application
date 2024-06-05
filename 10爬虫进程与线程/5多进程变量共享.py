import time
from multiprocessing import Process
"""
num = 1
def run1():
    # 声明num为全局变量
    global num
    num = 2  # 更改全局变量num的值为2
    print('我是run1函数', num)

run1()
print(num)
"""


List = []
def run1():
    List.append('lucky')
    print('我是run1函数', List)

run1()
print(List)
import threading
import time

def run(i):
    print('开启线程', i, threading.current_thread().name)
    time.sleep(2)

# 创建线程并起名称 传递参数  这个位置使用和进程一样
thr1 = threading.Thread(target=run, args=(1,), name='lucky-1')
thr2 = threading.Thread(target=run, args=(2,), name='lucky-2')
# print(thr)
thr1.start()
thr2.start()
thr1.join()
thr2.join()
print('开启线程', threading.current_thread().name)
print('over')
'''
每个进程会有一个默认主线程
在每个进程内开启的线程为子线程
MainThread
'''
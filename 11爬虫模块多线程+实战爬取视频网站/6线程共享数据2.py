import threading
import time

name = 'lucky'
def run():
    # time.sleep(2)
    global name
    name = '马冬梅'
    age = 18
    print(f'我叫:{name} 我今年{age}岁了', threading.current_thread().name)
def run1():
    age = 18
    print(f'我叫:{name} 我今年{age}岁了', threading.current_thread().name)
thr1 = threading.Thread(target=run, name='线程1')
thr2 = threading.Thread(target=run1, name='线程2')
thr1.start()
thr2.start()
thr1.join()
thr2.join()
print('我在外部获取数据', name)
print('over')

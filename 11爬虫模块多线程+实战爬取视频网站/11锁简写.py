import threading
lock = threading.Lock()
i = 0
def sum1():
    global i
    # 上锁
    with lock:
        for x in range(10000000):
            i += x
            i -= x
        # 释放锁
    print('sum1', i)

def sum2():
    global i
    # 上锁
    with lock:
        for x in range(10000000):
            i += x
            i -= x
        # 释放锁
    print('sum2', i)
thr1 = threading.Thread(target=sum1)
thr2 = threading.Thread(target=sum2)
thr1.start()
thr2.start()
thr1.join()
thr2.join()
print(i)
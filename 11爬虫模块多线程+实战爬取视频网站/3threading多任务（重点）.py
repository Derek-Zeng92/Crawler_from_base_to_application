import threading
import time


def run():
    print('线程开始')
    time.sleep(2)
    print('线程结束')

t1 = time.time()
# run()
# run()
# run()
# run()
# run()
thr_list = []
for i in range(5):
    # 创建线程
    thr = threading.Thread(target=run)
    # 开启线程
    thr.start()
    thr_list.append(thr)
    # thr.join()
# 线程等待
for i in thr_list:
    i.join()
print(time.time()- t1)
print('over')
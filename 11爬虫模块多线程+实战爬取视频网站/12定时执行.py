import threading


def run():
    print('执行了run函数')



# 定时执行 传入参数秒
thr = threading.Timer(3, run)
thr.start()
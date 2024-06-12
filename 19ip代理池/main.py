'''
项目运行入口文件
'''
from multiprocessing import Process
from get_ip import get_ip
from app import run
from test_ip import run as t_run


def main():
    Process(target=get_ip).start()  # 开启抓ip的进程
    Process(target=run).start()  # 开启获取ip的借口的进程
    Process(target=t_run).start()  # 开启测试ip的进程


if __name__ == '__main__':
    main()
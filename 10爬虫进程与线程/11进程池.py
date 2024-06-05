import time
from multiprocessing import Pool, cpu_count


def get_data(url):
    # 请求爬取数据
    # requests.get(url)
    # print(new_url)
    print('子进程开始', url)
    time.sleep(10)
    print('子进程结束', url)

if __name__ == '__main__':
    # 爬取10页数据
    # 注意
    # 自己练习抓取数据的时候 别给好几个进程  容易给网站跑死
    url = 'http://www.baidu.com?page='
    # pool = Pool()  # 传参 开启几个进程  默认开启核心数个cpu
    pool = Pool(10)  # 传参 开启几个进程  默认开启核心数个cpu
    for i in range(10):
        url = 'http://www.baidu.com?page='+str(i)
        # 任务添加到进程池
        pool.apply_async(get_data, args=(url, ))
    pool.close()  # 关闭池子 不在放进程了
    pool.join()  # 阻塞等待
    print('主进程结束')
    # print(cpu_count())

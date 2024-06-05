import time
from multiprocessing import Process


def get_data(url):
    # 请求爬取数据
    # requests.get(url)
    # print(new_url)
    print(url)
    time.sleep(1)

if __name__ == '__main__':
    # 爬取10页数据
    url = 'http://www.baidu.com?page='
    for i in range(10):
        new_url = url + str(i)
        Process(target=get_data, args=(new_url,)).start()

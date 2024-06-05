import time
from urllib.parse import urljoin

import requests
import os
from concurrent.futures import ThreadPoolExecutor, wait
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}


def down_video(url, i):
    '''
    下载ts文件
    :param url:
    :param i:
    :return:
    '''
    # print(url)
    # 下载ts文件
    resp = requests.get(url, headers=headers)
    with open(os.path.join(path, str(i) + '.ts'), mode="wb") as f3:
        f3.write(resp.content)
    # print('{} 下载完成！'.format(url))


def download_all_videos(path, host):
    '''
    下载m3u8文件以及多线程下载ts文件
    :param url:
    :param path:
    :return:
    '''
    if not os.path.exists(path):
        os.mkdir(path)
    # 开启线程 准备下载
    pool = ThreadPoolExecutor(max_workers=50)
    # 1. 读取文件
    tasks = []
    i = 0
    with open("index.m3u8", mode="r", encoding="utf-8") as f:
        for line in f:
            # 如果不是url 则走下次循环
            if line.startswith("#"):
                continue
            line = host + line
            print(line, i)
            # 开启线程
            tasks.append(pool.submit(down_video, line.strip(), i))
            i += 1
    # 统一等待
    wait(tasks)


# 处理m3u8文件中的url问题
def do_m3u8_url(url, path, m3u8_filename="index.m3u8"):
    # 这里还没处理key的问题
    if not os.path.exists(path):
        os.mkdir(path)

    with open(m3u8_filename, mode="r", encoding="utf-8") as f:
        data = f.readlines()

    fw = open(os.path.join(path, m3u8_filename), 'w', encoding='UTF-8')
    abs_path = os.getcwd()
    i = 0
    for line in data:
        # 如果不是url 则走下次循环
        if line.startswith("#"):
            # 判断处理是存在需要秘钥
            if line.find('URI') != -1:
                line = line.split('/')[0] + 'key.m3u8"\n'
                print(line)
                host = url.rsplit('/', 1)[0]
                # 爬取key
                download_m3u8(host + '/key.key', os.path.join(path, 'key.m3u8'))
            fw.write(line)
        else:
            fw.write(f'{abs_path}/{path}/{i}.ts\n')
            i += 1

def download_m3u8(url, m3u8_filename="index.m3u8"):
    print('正在下载index.m3u8文件')
    resp = requests.get(url, headers=headers)
    with open(m3u8_filename, mode="w", encoding="utf-8") as f:
        f.write(resp.content.decode('UTF-8'))

def merge(path, filename='output'):
    '''
    进行ts文件合并 解决视频音频不同步的问题 建议使用这种
    :param filePath:
    :return:
    '''
    os.chdir(path)
    cmd = f'ffmpeg -i index.m3u8 -c copy {filename}.mp4'
    os.system(cmd)

def get_m3u8_data(first_m3u8_url):
    session = requests.Session()

    # 请求第一次m3u8de url
    resp = session.get(first_m3u8_url, headers=headers)
    resp.encoding = 'UTF-8'
    data = resp.text

    # 第二次请求m3u8文件地址 返回最终包含所有ts文件的m3u8
    second_m3u8_url = urljoin(first_m3u8_url, data.split('/', 3)[-1].strip())
    resp = session.get(second_m3u8_url, headers=headers)
    with open('index.m3u8', 'w', encoding='UTF-8') as f:
        f.write(resp.content.decode('UTF-8'))
    return second_m3u8_url


if __name__ == '__main__':
    # ts文件存储目录
    path = 'ts'
    # 带加密的ts文件的 index.m3u8  url
    url = 'https://s7.fsvod1.com/20220622/5LnZiDXn/index.m3u8'
    meu8_url = get_m3u8_data(url)
    # 下载m3u8文件以及ts文件
    host = 'https://s7.fsvod1.com'   # 主机地址  用于拼凑完整的ts路径和秘钥路径
    # download_all_videos(path, host)
    do_m3u8_url(meu8_url, path)

    # 文件合并
    merge(path, '奇异博士')
    print('over')
from urllib.parse import urljoin

import requests
import os
from concurrent.futures import ThreadPoolExecutor, wait
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

def get_m3u8_url(url):
    '''
    通过页面的url 找到里面的m3u8地址进行请求  返回最终要的m3u8url与请求返回的文本内容
    :param url:
    :return:
    '''
    session = requests.Session()
    session.get('https://www.9meiju.cc/', headers=headers)
    # 请求电影网址

    resp = session.get(url, headers=headers)
    resp.encoding = 'UTF-8'
    data = resp.text
    first_m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')
    # 请求第一次m3u8de url
    resp = session.get(first_m3u8_url, headers=headers)
    resp.encoding = 'UTF-8'
    data = resp.text  # 获取到了第一次请求m3u8返回的内容

    # 第二次请求m3u8文件地址 返回最终包含所有ts文件的m3u8
    second_m3u8_url = urljoin(first_m3u8_url, data.split('/', 3)[-1].strip())
    resp = session.get(second_m3u8_url, headers=headers)
    with open('first.m3u8', 'w', encoding='UTF-8') as f:
        f.write(resp.content.decode('UTF-8'))
    return second_m3u8_url


def download_one_video(url, i, path):
    '''
    下载单个视频的函数
    :return:
    '''
    print(url, i,'开始下载')
    resp = requests.get(url, headers=headers)
    with open(os.path.join(path, f'{i}.ts'), 'wb') as f:
        f.write(resp.content)
    print(url, i,'完成下载')


def download_all_videos(path):
    '''
    下载所有视频的函数
    :return:
    '''
    if not os.path.exists(path):
        os.mkdir(path)
    # 读取index.m3u8的文件内容
    with open('first.m3u8', encoding='UTF-8') as f:
        data = f.readlines()
    # print(data)
    # 创建线程池
    pool = ThreadPoolExecutor(50)
    tasks = []
    i = 0
    for line in data:
        # 提取ts的url路径
        if line.startswith('#'):
            continue
        # 使用strip取出url结尾的换行符
        ts_url = line.strip()
        # 0.ts 1.ts 2.ts 3.ts ...
        tasks.append(pool.submit(download_one_video, ts_url, i, path))
        i += 1
    # 集体等待我们的线程对象执行完毕
    wait(tasks)


def merge(path, filename='output'):
    '''
    进行ts文件合并 解决视频音频不同步的问题 建议使用这种
    :param filePath:
    :return:
    '''
    os.chdir(path)   # 进入到当前的ts文件夹内
    cmd = f'ffmpeg -i first.m3u8 -c copy {filename}.mp4'
    os.system(cmd)

# 处理m3u8文件中的url问题
def do_m3u8_url(path, m3u8_filename="first.m3u8"):
    # 这里还没处理key的问题
    if not os.path.exists(path):
        os.mkdir(path)
    # else:
        # shutil.rmtree(path)
        # os.mkdir(path)
    with open(m3u8_filename, mode="r", encoding="utf-8") as f:
        data = f.readlines()
    fw = open(os.path.join(path, m3u8_filename), 'w', encoding="utf-8")
    abs_path = os.getcwd()
    i = 0
    for line in data:
        # 如果不是url 则走下次循环
        if line.startswith("#"):
            fw.write(line)
        else:
            fw.write(f'{abs_path}/{path}/{i}.ts\n')
            i += 1
# C:\Users\lucky\PycharmProjects\线上五期\14抓取网站视频与协程/ts/0.ts
if __name__ == '__main__':
    url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-1.html'
    # m3u8_url = get_m3u8_url(url)  # 请求返回index.m3u8的内容以及url
    path = 'ts'  # 存储ts文件的目录
    # download_all_videos(path)  # 下载所有ts文件
    # do_m3u8_url(path)
    merge(path, '闪电侠')  # 合并
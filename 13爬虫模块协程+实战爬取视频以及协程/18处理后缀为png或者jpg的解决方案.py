import shutil
import time
from urllib.parse import urljoin

import requests
import os
import re
from concurrent.futures import ThreadPoolExecutor, wait


def get_m3u8_url(url):
    '''
    获取页面中m3u8的url
    :param url: 电影页面的url
    :return:
    '''
    session = requests.Session()
    # 访问首页获取cookie
    session.get('https://www.9meiju.cc/', headers=headers)
    # url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-2.html'
    response = session.get(url, headers=headers)
    response.encoding = 'UTF-8'
    data = response.text
    # print(data)
    m3u8_uri = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')

    # 请求可以获取index.m3u8文件
    response = session.get(m3u8_uri, headers=headers)
    response.encoding = 'UTF-8'
    data = response.text
    # 拆分返回的内容获取真整的index.m3u8文件的url
    # 注意 一定要strip
    url = data.split('/', 3)[-1].strip()
    print(data)
    print('m3u8_uri', m3u8_uri)
    url = urljoin(m3u8_uri, url)
    print('url', url)
    return url


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


def download_all_videos(url, path):
    '''
    下载m3u8文件以及多线程下载ts文件
    :param url:
    :param path:
    :return:
    '''
    # 请求m3u8文件进行下载
    resp = requests.get(url, headers=headers)
    with open("index.m3u8", mode="w", encoding="utf-8") as f:
        f.write(resp.content.decode('UTF-8'))
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
            print(line, i)
            # 开启线程
            tasks.append(pool.submit(down_video, line.strip(), i))
            i += 1
    print(i)
    # 统一等待
    wait(tasks)


# 解析伪装成png的ts
def resolve_ts(src_path, dst_path):
    '''
    如果m3u8返回的ts文件地址为
    https://p1.eckwai.com/ufile/adsocial/7ead0935-dd4f-4d2f-b17d-dd9902f8cc77.png
    则需要下面处理后 才能进行合并
    原因在于 使用Hexeditor打开后，发现文件头被描述为了PNG
    在这种情况下，只需要将其中PNG文件头部分全部使用FF填充，即可处理该问题
    :return:
    '''
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    file_list = sorted(os.listdir(src_path), key=lambda x: int(x.split('.')[0]))
    for i in file_list:
        origin_ts = os.path.join(src_path, i)
        resolved_ts = os.path.join(dst_path, i)
        try:
            infile = open(origin_ts, "rb")  # 打开文件
            outfile = open(resolved_ts, "wb")  # 内容输出
            data = infile.read()
            outfile.write(data)
            outfile.seek(0x00)
            outfile.write(b'\xff\xff\xff\xff')
            outfile.flush()
            infile.close()  # 文件关闭
            outfile.close()
        except:
            pass
        print('resolve ' + origin_ts + ' success')

    else:
        # 删除目录
        shutil.rmtree(src_path)
        # 将副本重命名为正式文件
        os.rename(dst_path, dst_path.rstrip('2'))


# 处理m3u8文件中的url问题
def do_m3u8_url(path, m3u8_filename="index.m3u8"):
    # 这里还没处理key的问题
    if not os.path.exists(path):
        os.mkdir(path)

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


def merge(path, filename='output'):
    '''
    进行ts文件合并 解决视频音频不同步的问题 建议使用这种
    :param filePath:
    :return:
    '''
    os.chdir(path)
    cmd = f'ffmpeg -i index.m3u8 -c copy {filename}.mp4'
    os.system(cmd)


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    url = get_m3u8_url('https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-20.html')
    # 抓取99美剧闪电侠
    # ts文件存储目录
    path = 'ts'
    # 下载m3u8文件以及ts文件
    download_all_videos(url, path)
    # 合并png的ts文件
    src_path = path  # 要复制的文件路径
    dst_path = path + '2'  # 复制后的文件路径
    resolve_ts(src_path, dst_path)
    do_m3u8_url(src_path)
    merge(src_path, '闪电侠')
    print('over')

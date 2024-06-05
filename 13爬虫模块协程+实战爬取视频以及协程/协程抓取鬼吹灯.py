#!/usr/bin/python

import asyncio
import os
import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup


def get_page_source(web):
    '''
    返回页面的HTML内容
    :param web:
    :return:
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    response = requests.get(web, headers=headers)
    response.encoding = 'utf-8'
    return response.text


def parse_page_source(html):
    '''
    解析读取页面中'class': 'mulu-list quanji'的所有href超链接地址
    :param html:
    :return:
    '''
    book_list = []
    soup = BeautifulSoup(html, 'html.parser')
    a_list = soup.find_all('div', attrs={'class': 'mulu-list quanji'})
    for a in a_list:
        a_list = a.find_all('a')
        for href in a_list:
            chapter_url = href['href']
            book_list.append(chapter_url)
    return book_list


def get_book_name(book_page):
    '''
    通过传递进来的url 拆分成书book_number 和 book_chapter_name 值
    :param book_page:
    :return:
    '''
    book_number = book_page.split('/')[-1].split('.')[0]
    book_chapter_name = book_page.split('/')[-2]
    return book_number, book_chapter_name


async def aio_download_one(chapter_url, signal):
    number, c_name = get_book_name(chapter_url)
    # 如果当前请求出现了异常  重新请求10次！ 有一次成功就不循环了！！！！
    for c in range(10):
        try:
            # 控制协程的并发数据量
            async with signal:
                async with aiohttp.ClientSession() as session:
                    async with session.get(chapter_url) as resp:
                        page_source = await resp.text()
                        soup = BeautifulSoup(page_source, 'html.parser')
                        chapter_name = soup.find('h1').text
                        p_content = soup.find('div', attrs={'class': 'neirong'}).find_all('p')
                        content = [p.text + '\n' for p in p_content]
                        chapter_content = '\n'.join(content)
                        if not os.path.exists(f'{book_name}/{c_name}'):
                            os.makedirs(f'{book_name}/{c_name}')
                        async with aiofiles.open(f'{book_name}/{c_name}/{number}_{chapter_name}.txt', mode="w",
                                                 encoding='utf-8') as f:
                            await f.write(chapter_content)
                        print(chapter_url, "下载完毕!")
                        return ""
        except Exception as e:
            print(e)
            print(chapter_url, "下载失败!, 重新下载. ")
    return chapter_url


async def aio_download(url_list):
    tasks = []
    # 开启并发控制10
    semaphore = asyncio.Semaphore(10)
    for h in url_list:
        tasks.append(asyncio.create_task(aio_download_one(h, semaphore)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    url = 'https://www.51shucheng.net/daomu/guichuideng'
    book_name = '鬼吹灯'
    if not os.path.exists(book_name):
        os.makedirs(book_name)
    # 获取页面源代码
    source = get_page_source(url)
    # 解析页面中所有的超链接a
    href_list = parse_page_source(source)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aio_download(href_list))
    loop.close()
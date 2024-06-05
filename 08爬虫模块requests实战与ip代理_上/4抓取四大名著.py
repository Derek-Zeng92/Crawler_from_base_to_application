import random
import time

import requests
import os
from bs4 import BeautifulSoup
# 抓取四大名著


def get_html(main_url):
    '''
    获取HTML页面内容的方法
    :param main_url: 获取页面的url
    :return:
    '''
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    # 获取当前页面内容  返回四大名著标题和url
    # 三国演义/第一章节.text
    # 红楼梦/第一章节.text
    response = requests.get(main_url, headers=headers)
    response.encoding = response.apparent_encoding
    return BeautifulSoup(response.text, 'lxml')

def get_book(soup):
    '''
    获取4大名著的标题和url
    :param soup:
    :return:
    '''
    # 取出大名著标题和url
    div = soup.find_all('div', class_="book-item")
    book_dic = {}  # 存储书的字典 {书名:书链接}
    for con in div:
        # 获取书的名称
        book_name = con.get_text().replace('\n', '')
        # 获取url
        book_href = 'https://www.shicimingju.com' + con.a['href']
        book_dic[book_name] = book_href
    return book_dic


def get_book_mulu(books_html):
    '''
    抓取四大名著的章节  标题和href
    :param books_html: 当前章节的HTML内容
    :return:
    '''
    # 包含了整个章节的div
    div = books_html.find_all('div', class_="book-mulu")
    # 存储章节标题和url的字典
    mulu_dict = {}  # {章节: url}
    for mulu in div:
        # 抓取超链接
        mulu_hrefs = mulu.find_all('a')
        for mulu_href in mulu_hrefs:
            # 后去章节标题
            title = mulu_href.get_text()
            # 获取章节url
            href = mulu_href['href']
            mulu_dict[title] = 'https://www.shicimingju.com' + href
    return mulu_dict


def book_mulu_content(chapter, books_html):
    '''
    # 获取章节内容
    :param chapter:  标题
    :param books_html: 获取到的bs4对象的页面内容
    :return:
    '''
    con_dic = {}
    div = books_html.find('div', class_='chapter_content')
    text = div.text
    con_dic[chapter] = text
    return con_dic


def save_books(book_name, book_contents):
    '''
    存储文章内容
    :param book_name: 四大名著的书名 如：三国演义
    :param book_contents:  抓取到章节里面的内容
    :return:
    '''
    # 创建目录
    if not os.path.exists(book_name):
        os.mkdir(book_name)
    for title in book_contents:
        # 拼接路径
        path = os.path.join(book_name, title+'.text')
        # 进行存储
        with open(path, 'a', encoding='UTF-8') as f:
            f.write(book_contents[title])
            print(f'{book_name} === {title} 下载完成！！！！！')


def main(main_url):
    '''
    运行的主函数
    :param main_url:
    :return:
    '''
    # 里面包含了四大名著
    book_dic = get_book(get_html(main_url))
    # 循环获取到书名称  有了书名称就能获取到 url
    for book_name in book_dic:
        # 获取当前四大名著的章节
        mulu_dic = get_book_mulu(get_html(book_dic[book_name]))
        for title, url in mulu_dic.items():
            # 获取章节内容
            book_contents = book_mulu_content(title, get_html(url))
            save_books(book_name, book_contents)
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    main_url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
    main(main_url)

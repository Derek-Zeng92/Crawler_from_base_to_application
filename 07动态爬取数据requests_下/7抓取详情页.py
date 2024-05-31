import random
import time

import requests
from bs4 import BeautifulSoup
"""
1. 抓取单页影评
2. 抓取单页 展开的影评
3. 抓取单页当前影评的详情页
4. 抓取多页 展开的影评及详情页
"""

url = 'https://movie.douban.com/review/best/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
# 找到每条影评数据
div = soup.find_all('div', class_='main review-item')
# print(div)
for d in div:
    # 匹配详情页的链接
    href = d.a['href']
    response = requests.get(href, headers=headers)
    data = response.text
    # 进行详情页内容的处理
    detail_soup = BeautifulSoup(data, 'lxml')
    info = detail_soup.find('div', id='link-report').text
    # 匹配详情页里的简介
    print(href)
    print(info)
    time.sleep(random.randint(1,5))
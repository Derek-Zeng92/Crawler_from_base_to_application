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
    # 获取图片
    img = d.img
    # 获取标题
    title = d.h2.string
    # print(title)
    # 获取影评
    con = list(d.find('div', class_="short-content").stripped_strings)[0]
    print(con)
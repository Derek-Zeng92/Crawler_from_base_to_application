import random
import time
from lxml import etree
import requests

'''
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
https://movie.douban.com/top250?start=75&filter=
'''
# start怎么处理
# 1     0
# 2     25
# 3     50
# 4    75
# 10
# (页码 - 1) * 步长
# ( - 1)*25
# 要5页数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
for i in range(1, 6):
    # 如果当前代码有错 添加异常处理
    try:
        start = (i - 1) * 25
        # 动态拼接url
        url = f'https://movie.douban.com/top250?start={start}&filter='
        print(f'第{i}页数据')
        response = requests.get(url, headers=headers)
        # print(response.text)
        tree = etree.HTML(response.text)
        # 匹配到每个电影的li里面的div
        div = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div')
        # print(div)
        for d in div:
            # 获取当前电影序号
            num = d.xpath('./div/em/text()')[0]
            # 获取电影标题
            title = d.xpath('.//span[@class="title"][1]/text()')[0]
            print(num, title)
    except Exception as e:
        print(e, url)

    time.sleep(random.randint(1,3))
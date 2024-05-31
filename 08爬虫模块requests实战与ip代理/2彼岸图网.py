import os.path
import random
import time
import requests
from lxml import etree
from urllib import request as req


def main(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'GBK'
    # print(response.text)
    tree = etree.HTML(response.text)
    # 获取到了当前所有的图片的li
    li = tree.xpath('//ul[@class="clearfix"]/li')
    for i in li:
        # 后去图片url
        href = i.xpath('./a//img/@src')
        # 拼凑完整url
        image_url = 'http://pic.netbian.com' + href[0]
        image_name = i.xpath('./a/b/text()')[0]
        # print(image_url)
        path = './img'
        # 如果当前路径不存在 则创建
        if not os.path.exists(path):
            os.mkdir(path)
        req.urlretrieve(image_url, os.path.join(path, image_name+'.jpg'))
        print(image_name)
        time.sleep(random.randint(1,3))


if __name__ == '__main__':
    url = 'http://pic.netbian.com/'
    main(url)
# 1 练习 抓取多页
# 2 练习 抓取详情页的大图
# 3 练习 抓取多页 详情页的大图


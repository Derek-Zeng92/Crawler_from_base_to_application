import random
import time
from lxml import etree
import requests
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

req = requests.get(url,headers=headers)
# req.encoding = 'GBK'
req.encoding = req.apparent_encoding  # 自动识别编码
# print(req.text)
tree = etree.HTML(req.text)
# 获取标题
title_list = tree.xpath('//div[@class="book-mulu"]/ul/li/a/text()')
# 获取超链接
href_list = tree.xpath('//div[@class="book-mulu"]/ul/li/a/@href')
for i in range(len(title_list)):
        # print(title_list[i])
        url = 'https://www.shicimingju.com' + href_list[i]
        print(url)
        req = requests.get(url, headers=headers)
        req.encoding = req.apparent_encoding  # 自动识别编码
        # print(req.text)
        tree = etree.HTML(req.text)
        con = tree.xpath('//div[@class="card bookmark-list"]//text()')
        print(title_list[i])
        print(con)
        time.sleep(random.randint(1,4))
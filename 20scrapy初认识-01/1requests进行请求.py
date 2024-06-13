import requests
from lxml import etree
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
url = 'https://duanzixing.com/'
# 进行请求
res = requests.get(url, headers=headers)
# 解码
html = res.content.decode()
# print(html)
tree = etree.HTML(html)
# 抓取每个article
article_list = tree.xpath('//article[@class="excerpt"]')
# print(article_list)
# 循环后去每一个article
for article in article_list:
    # 抓取标题
    title = article.xpath('./header/h2/a/text()')
    # 抓取内容
    con = article.xpath('./p[@class="note"]/text()')
    print(title, con)
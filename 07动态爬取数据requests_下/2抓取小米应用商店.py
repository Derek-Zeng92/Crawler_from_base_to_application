import requests
from lxml import etree

url = 'https://app.mi.com/catTopList/0?page=1'
response = requests.get(url)
response.encoding = 'UTF-8'
# print(response.text)
tree = etree.HTML(response.text)
#  匹配应用名称
# app_name = tree.xpath('//ul[@class="applist"]/li/h5/a/text()')
# print(app_name)

# 匹配应用链接
# link = tree.xpath('//ul[@class="applist"]/li/h5/a/@href')
# print(link)

# 匹配名称 和 链接呢
val = tree.xpath('//ul[@class="applist"]/li/h5/a/text() | //ul[@class="applist"]/li/h5/a/@href')
print(val)
'''
[1, 2, 3, 4]
0 1
2 3
'''
# print('href', '名称')
for i in range(0, len(val), 2):
    print('href', 'https://app.mi.com'+val[i], '名称', val[i+1])
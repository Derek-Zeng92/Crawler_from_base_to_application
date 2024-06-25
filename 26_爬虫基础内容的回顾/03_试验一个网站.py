import requests
from lxml import etree

url = "http://www.boxofficecn.com/boxoffice2019"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
# print(resp.text)

# //table/tbody/tr/td

tree = etree.HTML(resp.text)
result = tree.xpath("//table/tbody/tr")
for tr in result:  # 尽量的一条一条数据为单位进行处理.
    xv = tr.xpath("./td[1]//text()")
    nian = tr.xpath("./td[2]//text()")
    ming = tr.xpath("./td[3]//text()")
    qian = tr.xpath("./td[4]//text()")
    print(xv, nian, ming, qian)

# 第一条数据
# 第二条数据
# 第三条数据



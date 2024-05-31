import requests
from bs4 import BeautifulSoup

# url地址
url = 'https://cang.cngold.org/c/2022-06-14/c8152503.html'
# 请求网址
response = requests.get(url)
# 设置编码
response.encoding = 'UTF-8'
# 获取HTML内容
html = response.text
# 实例化bs4对象
soup = BeautifulSoup(html, 'lxml')
# 解析 匹配
# 因为当前table的border为1  所有查找的时候 我们要限定
table = soup.find('table', attrs={'border': "1"})
# print(table)
# 查找所有tr
tr = table.find_all('tr')
for t in tr:
    td = t.find_all('td')
    print('名称' ,td[0].text, '品相', td[1].text, '价格', td[2].text)
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
# 实例化
soup = BeautifulSoup(html_doc, 'lxml')
# print(soup)
# print(type(soup))  # <class 'bs4.BeautifulSoup'>
# soupd对象.标签名称
# print(soup.title)
# 获取当前标签名
# print(soup.title.name)
# 获取标签里的内容
# print(soup.title.string)
# print(soup.title.text)

# print(soup.p)
# print(soup.p['class'])  # 获取class属性值
# print(soup.p['class'])

# print(soup.a)
# 获取所有a标签
# print(soup.findAll("a"))

# print(soup.findAll("a"))
# 查找id为link3的标签
print(soup.findAll(id="link3"))

print(soup.get_text())


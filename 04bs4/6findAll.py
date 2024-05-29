import re

html_doc = """
<html><head><b>不不不不不</b><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
<p class="abc">...</p>
<p class="abc" id="efg">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.find_all("p"))
# print(soup.find_all("p", "story"))

# 匹配class属性值为abc
# print(soup.find_all(class_="abc"))
# 找到包含the的字符串文本
# print(soup.find(string=re.compile("The")))


# 因为第一个参数就是name  所以不给关键字 就是按照标签匹配
# 匹配以b作为开头的节点
# print(list(soup.find_all(re.compile('^b'))))
# for i in soup.find_all(re.compile('^b')):
#     print(i)

# 匹配多个列表
# 匹配所有a标签和b标签
# print(list(soup.find_all(['a', 'b'])))
# print(list(soup.find_all(['a', re.compile('^b')])))

# 关键字
# print(soup.find_all(id="link1"))
# print(soup.find_all(class_="abc"))
# print(soup.find_all(class_="abc", id="efg"))
# 等同于上方
# print(soup.find_all(attrs={'class':"abc", 'id':'efg'}))
# print(soup.find_all(class_=True))

# print(soup.find_all('a', limit=2))
# print(soup.find_all('a', limit=5))
# print(soup.find_all('a')[0:2])


# print(list(soup.find('a')))
# print(soup.find(text="Elsie").find_parent())
# print(soup.find("p", class_="abc").find_parent())
print(soup.find("p", class_="abc").find_parents())


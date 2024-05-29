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
<p class="abc def">...</p>
<p class="abc" id="efg"><i>i标签</i></p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# 查找所有a标签
# print(soup.select('a'))
# print(soup.select('b'))

# 匹配class选择器值为sister
# print(soup.select('.sister'))
# print(soup.select('#link1'))



# 匹配 class="abc" id="efg"
# print(soup.select('.abc#efg'))

# 匹配 class="abc" id="efg" 里面的i标签
# print(soup.select('.abc#efg i'))

# 匹配class值为abc和def的
# print(soup.select('.abc.def'))

# 查找p标签class属性值为story的节点
print(soup.select('p[class="story"]'))
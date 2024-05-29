import re
"""
需求
1. 豆瓣图书标题
2. 抓取图片的标签
"""

# 读取数据
f = open('豆瓣.html','r')
data = f.read()
f.close()
"""
<a href="https://book.douban.com/subject/27104959/">离开的，留下的</a>
<a href="https://book.douban.com/subject/26961102/">灵契</a>
<a href="https://book.douban.com/subject/27054039/">寓言</a>
<a href="https://book.douban.com/subject/27139971/">高难度对话：如何与挑剔的人愉快相处</a>
"""
# 正则匹配所有标题
# pattern = re.compile('<a href="https://book.douban.com/subject/\d+/">(.*?)</a>')
# titleList = pattern.findall(data)
# print(titleList)


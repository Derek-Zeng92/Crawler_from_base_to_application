from bs4 import BeautifulSoup
soup = BeautifulSoup(open('../素材/豆瓣.html', 'r',encoding="utf-8"), 'lxml')

# 匹配图片地址
print(soup.find_all('img'))
for i in soup.find_all('img'):
    print(i.attrs)  # 获取图片连接地址

# 获取标题 简介 评分等信息
"""
h = soup.find_all('div', class_='detail-frame')
for i in h:
    # print(i.text)  # 获取当前节点里所有的文本内容
    print(i.a.text)  # 获取标题  超链接里面的文本内容
    print(i.find('span', class_='font-small color-lightgray').text)  # 获取评分
    print(i.find('p', 'color-gray').text)  # 获取简介
    print(i.find_all('p')[-1].text)  # 获取简介
"""

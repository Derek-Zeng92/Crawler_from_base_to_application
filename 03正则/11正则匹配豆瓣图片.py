import re
f = open('./素材/豆瓣.html', 'rb')
data = f.read().decode('UTF-8')
f.close()
# 匹配图片
# <img src="https://img3.doubanio.com/mpic/s29554772.jpg"/>
# <img src="https://img3.doubanio.com/mpic/s29590893.jpg"/>
# <img src="https://img3.doubanio.com/mpic/s29578984.jpg"/>

pattern = re.compile('<img src="https://img\d\.doubanio.com/mpic/\w+\.jpg"/>')
# print(pattern.findall(data))
# 存储到文件中
with open('./img.html', 'w') as f:
    f.writelines(pattern.findall(data))
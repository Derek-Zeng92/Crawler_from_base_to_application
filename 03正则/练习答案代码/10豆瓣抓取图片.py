import re
path = r"C:\Users\xlg\Desktop\豆瓣.html"
file = open(path,"rb")
data = file.read().decode("utf-8")
file.close()

# print(data)
# <img src="https://img3.doubanio.com/mpic/s29590893.jpg"/>
# <img src="https://img3.doubanio.com/mpic/s29578984.jpg"/>
# pattern = re.compile("<img src=\"https://img3.doubanio.com/mpic/s\d{8}\.jpg\"/>")
pattern = re.compile("<img src=\"https://img[0-9]\.doubanio.com/mpic/\w+\.jpg\"/>")
imgList = pattern.findall(data)

# <img src="https://img1.doubanio.com/mpic/s29533317.jpg"/>
path = r"C:\Users\xlg\Desktop\img.html"
file = open(path,"w")
file.writelines(imgList)
file.close()

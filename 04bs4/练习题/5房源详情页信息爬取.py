from bs4 import BeautifulSoup

soup = BeautifulSoup(open('../素材/二手房详情页.html', 'r',encoding="utf-8"), 'lxml')
# 通过select方式进行获取
# sidefixedbox = soup.select('.sidefixedbox#sidefixedbox')
# print(sidefixedbox[0].text)
# 通过属性
sidefixedbox = soup.find('div', attrs={'class': 'sidefixedbox', 'id': 'sidefixedbox'}).text
print(sidefixedbox)
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('../素材/广州二手房.html', 'r',encoding="utf-8"), 'lxml')
# 二手房源信息
# ps = soup.find_all('div', class_='item-info fl')
ps = soup.find_all('div', class_='house-item house-itemB clearfix')
for p in ps:
    # 获取标题
    title = p.select('.cBlueB')[0].text
    house_name = p.select('.house-name')[0].text
    house_txt1 = p.select('.house-txt')[0].text
    house_txt2 = p.select('.house-txt')[1].text
    # 获取右侧价格
    price = p.select('.item-pricearea.fr')[0].text
    # price = p.find('div', class_='item-pricearea fr').text
    print(title, house_name, house_txt1, house_txt2, price)
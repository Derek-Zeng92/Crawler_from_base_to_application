from bs4 import BeautifulSoup
# 枫叶小说网
con = open('../素材/请仙儿(夜白)最新章节吧_请仙儿全文阅读_枫叶小说网.html', 'r', encoding='GBK')
soup = BeautifulSoup(con, 'lxml')
# 抓取全部章节
# print(soup.find('ul',class_='list-group list-charts'))

# 抓取请仙儿说明
# print(soup.find('div',class_='panel-body book-ext-info').text)

# 抓取猜你喜欢
# print(soup.find_all('ul', class_='list-group list-charts')[-1].find_all('a'))
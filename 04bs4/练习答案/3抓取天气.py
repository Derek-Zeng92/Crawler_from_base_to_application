from bs4 import BeautifulSoup
ALL_DATA = []
soup = BeautifulSoup(open('../素材/匹配天气.html', 'r',encoding="utf-8"), 'lxml')
conMidtab = soup.find('div',class_='conMidtab')
# 获取所有的天气信息表格
tables = conMidtab.find_all('table')
for table in tables:
    # 过滤掉标题行
    trs = table.find_all('tr')[2:]
    for index, tr in enumerate(trs):
        tds = tr.find_all('td')
        # print(index, tds)
        # 获取城市和天气
        city_td = tds[0]
        temp_td = tds[3]
        # 过滤掉表格左侧的省/直辖市
        if index == 0:
            city_td = tds[1]
            temp_td = tds[4]
        city_td = list(city_td.stripped_strings)[0]
        temp_td = list(temp_td.stripped_strings)[0]
        ALL_DATA.append({'city':city_td,'temp':temp_td})

print(ALL_DATA)



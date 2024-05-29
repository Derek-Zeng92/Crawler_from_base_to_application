from bs4 import BeautifulSoup

# 进行请求
# 获取页面内容
con = open('../素材/三国演义.html', 'r',encoding="utf-8")
# 参数 页面内容  解析器
soup = BeautifulSoup(con, 'lxml')
title_list = soup.select('.book-mulu>ul>li>a')

with open('./爬取三国演义.html', 'w', encoding='GBK') as f:
    for t in title_list:
        # 输出文章标题
        title = t.text
        # 获取文章地址
        href = t['href']
        url = 'https://www.shicimingju.com/'+href
        print(url)
        f.write(f"<a href='{url}' target='_blank'>{title}</a>"+'<br />')
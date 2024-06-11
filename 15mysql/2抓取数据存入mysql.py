import requests
from lxml import etree
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='test')
# print(db)
# 设置字符编码
db.set_charset('utf8')
# 创建游标对象  用于下面的操作
cursor = db.cursor()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
url = 'https://www.shortarticle.cn/sanwen/'
res = requests.get(url, headers=headers)
data = res.content.decode()
# print(data)
tree = etree.HTML(data)
# 获取所以超链接的url
a_list = tree.xpath('//*[@id="ct"]/div[1]/div[2]/div/div[2]/li/a')
# print(a_list)
for a in a_list:
    a_url = 'https://www.shortarticle.cn' + a.get('href')

    res = requests.get(a_url, headers=headers)
    tree = etree.HTML(res.content.decode())
    # 标题
    title = tree.xpath('//*[@id="ct"]/div[1]/div[2]/div[1]/div[1]/h1/text()')[0]
    # 作者
    author = tree.xpath('//*[@id="ct"]/div[1]/div[2]/div[1]/div[2]/span[1]/text()')[0]
    # 文章
    articles = tree.xpath('//*[@id="article_content"]/text()')
    article = ', '.join(str(item) for item in articles)
    article = ''.join(article).replace('"', '')  # 处理文章中的双引号 防止和外层的引号发生冲突 这样数据就会写入失败
    try:
        # 插入数据
        sql = f'insert into article values(null, "{title}", "{author}", "{article}")'
        cursor.execute(sql)
        print(cursor.rowcount)  # 受影响的行数
        db.commit()  # 提交事务
    except:
        db.rollback()  # 回滚事务

db.close()  # 关闭数据库连接

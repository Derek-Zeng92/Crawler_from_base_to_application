# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class DuanziMysqlPipeline:
    # 爬虫开启时运行一次
    def open_spider(self, item):
        # 数据库的连接
        self.db = pymysql.connect(host='127.0.0.1', port=3306, db='lucky', user='root', password='123456', charset='utf8')
        # 创建游标对象
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        try:
            # 拼接SQL
            sql = f'insert into duanzi(title, con) values("{item["title"]}", "{item["con"]}")'
            # 执行SQL语句
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e, sql)
            self.db.rollback()
        return item

    def close_spider(self, item):
        # 关闭mysql连接
        self.db.close()
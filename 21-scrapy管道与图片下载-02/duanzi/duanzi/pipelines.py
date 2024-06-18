# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import pymysql


class DuanziPipeline:
    def process_item(self, item, spider):
        return item



class DuanzimongoPipeline:
    def open_spider(self, spider):
        # 连接数据库
        self.con = MongoClient(host='127.0.0.1', port=27017)
        # 选择集合
        self.collection = self.con.spider.duanzi

    def process_item(self, item, spider):
        # 插入数据
        self.collection.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        # 关闭mongo连接
        self.con.close()


class DuanzimysqlPipeline:
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


class DuanzifilePipeline:
    # 开启爬虫的时候执行一次
    def open_spider(self, item):
        self.f = open('duanzi.txt', 'w', encoding='UTF-8')
    # 实现对item数据的处理
    def process_item(self, item, spider):
        # 取出item对象中的数据
        self.f.write(item['title']+'\n')
        self.f.write(item['con']+'\n')
        return item
    # 关闭爬虫的时候执行一次
    def close_spider(self, item):
        self.f.close()

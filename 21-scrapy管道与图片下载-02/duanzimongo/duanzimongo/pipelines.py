# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

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
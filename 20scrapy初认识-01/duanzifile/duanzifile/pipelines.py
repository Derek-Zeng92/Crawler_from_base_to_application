# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 管道要使用的话主要要在settings中开启
class DuanzifilePipeline:
    # 开启爬虫的时候执行一次
    def open_spider(self, item):
        self.f= open('duanzi.txt','w',encoding='utf-8')

    # 实现对item数据的处理
    def process_item(self, item, spider):
        # 获取item对象中的数据
        self.f.write(item['title']+'\n')
        self.f.write(item['con']+'\n')
        return item
    # 关闭爬虫的时候执行一次
    def close_spider(self, item):
        self.f.close()

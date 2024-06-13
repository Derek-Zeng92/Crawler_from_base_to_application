# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DuanzifileItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义了要储存的字段title和con  那你就只能存这两个字段 存进其他字段则报错
    title=scrapy.Field()
    con=scrapy.Field()

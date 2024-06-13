import scrapy
from duanzi_mysql.items import DuanziMysqlItem  # 导入字段类

class DuanziSpider(scrapy.Spider):
    name = "duanzi"
    allowed_domains = ["duanzixing.com"]
    start_urls = ["https://duanzixing.com"]

    def parse(self, response, **kwargs):
        item = DuanziMysqlItem()  # 实例化
        # 获取每个段子的article标签
        article_list = response.xpath('//article[@class="excerpt"]')
        for article in article_list:
            # 抓取标题
            title = article.xpath('./header/h2/a/text()').extract_first()
            # 抓取内容
            con = article.xpath('./p[@class="note"]/text()').extract_first()
            item['title'] = title
            item['con'] = con
            yield item

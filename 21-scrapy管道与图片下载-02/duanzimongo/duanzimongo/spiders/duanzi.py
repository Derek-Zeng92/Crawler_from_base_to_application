import scrapy
from duanzimongo.items import DuanzimongoItem

class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    allowed_domains = ['duanzixing.com']
    start_urls = ['http://duanzixing.com/']

    def parse(self, response, **kwargs):
        # 获取每个段子的article标签
        article_list = response.xpath('//article[@class="excerpt"]')
        for article in article_list:
            item = DuanzimongoItem()  # 实例化
            dic_data = {}
            # 获取标题
            title = article.xpath('./header/h2/a/text()').extract_first()
            # 获取内容
            con = article.xpath('./p[@class="note"]//text()').extract_first()
            # print(con)
            item['title'] = title
            item['con'] = con
            yield item
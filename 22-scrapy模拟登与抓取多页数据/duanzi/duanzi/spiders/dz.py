import scrapy
from duanzi.items import DuanziItem

class DzSpider(scrapy.Spider):
    name = 'dz'
    allowed_domains = ['duanzixing.com']
    start_urls = ['http://duanzixing.com/']

    def parse(self, response, **kwargs):
        # https://duanzixing.com/page/3/
        # https://duanzixing.com/page/5/
        url = 'https://duanzixing.com/page/%d/'
        # 抓10页数据
        for i in range(1, 11):
            new_url = url%i
            # 请求每页的url
            yield scrapy.Request(new_url, callback=self.parse_detail)

    def parse_detail(self, response, **kwargs):
        '''
        解析页面详情提取数据的方法
        '''
        # print(response.text)
        article_list = response.xpath('//article[@class="excerpt"]')
        for article in article_list:
            item = DuanziItem()
            title = article.xpath('./header/h2/a/text()').extract_first()
            con = article.xpath('./p[@class="note"]/text()').extract_first()
            # print(response.url, title, con)
            item['title'] = title
            item['con'] = con
            print(item)
            yield item
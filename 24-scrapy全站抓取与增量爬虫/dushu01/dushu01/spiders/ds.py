import scrapy
from dushu01.items import Dushu01Item


class DsSpider(scrapy.Spider):
    name = 'ds'
    # allowed_domains = ['www.dushu.com/book/1188_1.html']
    start_urls = ['http://www.dushu.com/book/1188_1.html']


    def parse(self, response, **kwargs):
        # 解析 获取详情页的url
        detail_url_list = response.xpath('//div[@class="bookslist"]/ul/li/div/div/a/@href').extract()
        # print(detail_url_list)
        for dl in detail_url_list:
            # 拼凑详情页的url
            detail_url = response.urljoin(dl)
            yield scrapy.Request(detail_url, callback=self.parse_detail)

        # 抓取多页
        for page in range(2, 1000):
            url = f'https://www.dushu.com/book/1188_{page}.html'
            yield scrapy.Request(url, callback=self.parse)

    # 解析详情页数据的方法
    def parse_detail(self, response):
        if not response.text:
            return
        item = Dushu01Item()
        # 解析详情页中的数据
        title = response.xpath('//div[@class="book-title"]/h1/text()').extract_first()
        info = ''.join(response.xpath('//div[@class="text txtsummary"]/text()').extract())
        # print(title, info)
        item['title'] = title
        item['info'] = info
        print(item)
        yield item
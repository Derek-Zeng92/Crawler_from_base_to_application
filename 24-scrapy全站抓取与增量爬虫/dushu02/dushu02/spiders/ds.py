import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DsSpider(CrawlSpider):
    name = 'ds'
    # allowed_domains = ['www.dushu.com/book/1188_1.html']
    start_urls = ['http://www.dushu.com/book/1188_1.html']

    rules = (
        # 抓取分页
        Rule(LinkExtractor(allow=r'book/1188_\d+.html'), follow=True),
        # 查找详情的url的规则
        Rule(LinkExtractor(allow=r'/book/\d+/$'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        item = {}
        title = response.xpath('//div[@class="book-title"]/h1/text()').extract_first()
        info = ''.join(response.xpath('//div[@class="text txtsummary"]/text()').extract())
        # print(title, info)
        item['title'] = title
        item['info'] = info
        print(item)
        return item

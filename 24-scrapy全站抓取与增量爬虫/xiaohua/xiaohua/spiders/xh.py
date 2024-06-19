import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class XhSpider(CrawlSpider):
    name = 'xh'
    # allowed_domains = ['www.xiaohua.com']
    start_urls = ['http://www.xiaohua.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # 匹配页码
        # Rule(LinkExtractor(allow=r'/hot\?page=\d+'), callback='parse_page', follow=False),
        # Rule(LinkExtractor(allow=r'/hot\?page=\d+'), callback='parse_page', follow=True),
        # 匹配所有  所有的超链接都会给你返回
        # Rule(LinkExtractor(allow=r''), callback='parse_page', follow=True),
        # 匹配详情页的url
        Rule(LinkExtractor(allow=r'/detail/\d+'), callback='parse_page_detail', follow=True),
    )

    # 解析页码进行回调
    def parse_page_detail(self, response):
        item = {}
        print(response)  # 返回的为响应对于  是对于当前符合规则url的再次请求
        print(repr(''.join(response.xpath('//text()').extract())))  # 对于响应的再次进行xpath  提取出你要的数据
        return item

    # 解析页码进行回调
    def parse_page(self, response):
        item = {}
        print(response)
        return item



    def parse_item(self, response):
        item = {}
        print(response)
        return item

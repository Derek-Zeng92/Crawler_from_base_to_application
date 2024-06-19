import scrapy
from duanzi.items import DuanziItem
from redis import Redis

class DzSpider(scrapy.Spider):
    name = 'dz'
    allowed_domains = ['duanzixing.com']
    start_urls = ['http://duanzixing.com/']
    # 连接redis
    redis = Redis(host='127.0.0.1', port=6379, password='123456')

    def parse(self, response, **kwargs):
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
            # 抓取每个段子详情的url
            href = article.xpath('./header/h2/a/@href').extract_first()
            # 扔到redis中
            if self.redis.sadd('urls', href) == 1:
                print('抓取到了新数据')
                item = DuanziItem()
                title = article.xpath('./header/h2/a/text()').extract_first()
                con = article.xpath('./p[@class="note"]/text()').extract_first()
                # print(response.url, title, con)
                item['title'] = title
                item['con'] = con
                print(item)
                yield item
            else:
                print('当前无数据更新')
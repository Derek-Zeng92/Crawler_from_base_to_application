import scrapy
from scrapy_redis.spiders import RedisSpider  # 导入分布式的spider


# class DsSpider(scrapy.Spider):
class DsSpider(RedisSpider):
    name = 'ds'
    # allowed_domains = ['dushu.com']
    # start_urls = ['https://www.dushu.com/book/1188_1.html']
    redis_key = 'dushu'  # 代替你的start_urls的，我们将url扔进叫这个名字的redis中
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
        item = {}
        # 解析详情页中的数据
        title = response.xpath('//div[@class="book-title"]/h1/text()').extract_first()
        info = ''.join(response.xpath('//div[@class="text txtsummary"]/text()').extract())
        # print(title, info)
        item['title'] = title
        item['info'] = info
        print(item)
        yield item

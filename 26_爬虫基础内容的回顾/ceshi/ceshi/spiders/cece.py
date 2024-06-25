import scrapy
from scrapy import Request


class CeceSpider(scrapy.Spider):
    name = 'cece'
    allowed_domains = ['17k.com']
    start_urls = []

    # 重写start_requests. 在启动时自动执行
    def start_requests(self):
        # don't filter 不过滤
        # 需要反复的. 重复的去请求一个url
        yield Request('https://www.17k.com/all', dont_filter=True)
        yield Request('https://www.17k.com/all', dont_filter=True)

    def parse(self, response):
        print("我收到了响应信息")

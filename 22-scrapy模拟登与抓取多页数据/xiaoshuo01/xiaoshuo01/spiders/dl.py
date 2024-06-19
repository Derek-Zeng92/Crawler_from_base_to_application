import scrapy


class DlSpider(scrapy.Spider):
    name = 'dl'
    allowed_domains = ['17k.com']
    start_urls = ['https://user.17k.com/ck/user/myInfo/96139098?bindInfo=1&appKey=2406394919']

    def parse(self, response, **kwargs):
        print(response.text)

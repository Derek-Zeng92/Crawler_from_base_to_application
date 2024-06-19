# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import time
from scrapy.http import HtmlResponse
from wangyi.settings import USER_AGENTS_LIST
import random

class WangyiSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WangyiDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        ua = random.choice(USER_AGENTS_LIST)  # 每次的请求头都不同
        request.headers['User-Agent'] = ua  # 设置请求头

        # 隧道代理使用
        proxy = "XXX.kdlapi.com:15818"
        # 用户名密码认证
        username = "username"
        password = "password"
        request.meta['proxy'] = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy}
        request.headers["Connection"] = "close"
        return None

    def process_response(self, request, response, spider):
        driver = spider.driver  # 获取爬虫中的driver属性
        # 如果是板块的url我们就进行抓取
        if request.url in spider.page_url:
            driver.get(request.url)  # 使用selenium抓取刚才的请求
            # 滚动条滚动到最下方
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(1)
            # 拖动两次
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(1)
            text = driver.page_source  # 获取页面源代码
            # 构造HTML响应  篡改响应
            return HtmlResponse(url=request.url, body=text, request=request, encoding='UTF-8')
        return response

    def process_exception(self, request, exception, spider):

        print('process_exception')
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

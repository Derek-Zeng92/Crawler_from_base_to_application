import scrapy
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options


class WySpider(scrapy.Spider):
    name = 'wy'
    # allowed_domains = ['news.163.com/domestic/']
    start_urls = ['http://news.163.com/domestic/']
    li_index = [1, 2]  # 索引为1 和2的url为国内和国际板块的url
    page_url = []  # 里面存放的为板块的url
    # 隐藏浏览器界面
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--disable-gpu')
    # 防止检测
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 导入配置
    driver = Chrome(chrome_options=chrome_option, options=option)


    def parse(self, response, **kwargs):
        # 抓取国内和国际板块的数据
        # 返回了所有的板块的url
        url_list = response.xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li/a/@href').extract()
        # print(url_list)
        for i in range(len(url_list)):
            if i in self.li_index:
                url = url_list[i]
                # 把板块对应的url存放起来
                self.page_url.append(url)
                yield scrapy.Request(url, callback=self.parse_detail)

    # 对于板块请求后的处理
    def parse_detail(self, response):
        # 抓取所有新闻对应详情页的url
        url_list = response.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/div/a/@href').extract()
        print(url_list)
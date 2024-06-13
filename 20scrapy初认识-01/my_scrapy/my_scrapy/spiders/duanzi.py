import scrapy


class DuanziSpider(scrapy.Spider):
    name = "duanzi" # 爬虫名字
    allowed_domains = ["duanzixing.com"] #允许爬取的域名
    start_urls = ["https://duanzixing.com"] # 其实抓取的url地址

    # 解析  必须叫这个名字 你不能动
    # def parse(self, response, **kwargs):
    #     # 解析页面源代码
    #     print(response.text)
    #     #  响应体，也就是html代码，byte类型
    #     print(response.body)
    #     # 当前响应的url地址
    #     print(response.url)
    #     # 当前响应对应的请求的url地址
    #     print(response.request.url)
    #     # 当前响应的请求头
    #     print(response.headers)
    #     # 当前响应的请求头
    #     print(response.request.headers)
    #     # 响应状态码
    #     print(response.status)

    def parse(self, response, **kwargs):
        # 获取每个段子的article标签
        article_list=response.xpath('//article[@class="excerpt"]')
        for article in article_list:
            dic_data={}
            # 抓取标题
            title=article.xpath('./header/h2/a/text()').extract_first()
            # 抓取内容
            con = article.xpath('./p[@class="note"]/text()').extract_first()
            dic_data['title']=title
            dic_data['con']=con
            yield dic_data
            print(title,con)
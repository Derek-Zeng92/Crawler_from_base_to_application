import scrapy


class WxSpider(scrapy.Spider):
    name = 'wx'
    # allowed_domains = ['ks.wangxiao.cn']
    start_urls = ['http://ks.wangxiao.cn/']

    def parse(self, response, **kwargs):
        # 每个一级标题的li的列表
        li_list = response.xpath('//ul[@class="first-title"]/li')
        for li in li_list:
            # 获取到一级标题
            one_title = li.xpath('./p/span/text()').extract_first()  # 对于当前的每一个一级标题再次进行xpath提取数据
            # print(one_title)
            # 获取二级标题的a标签的列表
            two_title_a_list = li.xpath('./div[@class="send-title"]/a')
            for a in two_title_a_list:
                two_title = a.xpath('./text()').extract_first()  # 获取的为二级标题
                # 拼凑成完整的二级标题的url 并替换url为考点练习的url
                two_title_url = response.urljoin(a.xpath('./@href').extract_first()).replace('TestPaper', 'exampoint')  # 二级标题的url
                '''
                http://ks.wangxiao.cn/TestPaper/list?sign=jz1
                http://ks.wangxiao.cn/exampoint/list?sign=jz1  # 考点练习的url
                '''
                # print(one_title, two_title, two_title_url)
                # yield scrapy.Request(two_title_url, meta={'one_title': one_title, 'two_title': two_title}, callback=self.two_parse)
        yield scrapy.Request('https://ks.wangxiao.cn/exampoint/list?sign=jz1', meta={'one_title': '工程类', 'two_title': '一级建造师'}, callback=self.two_parse)
    # 对于二级url的解析处理
    def two_parse(self, response):
        # 通过meta传递  获取到一级标题
        one_title = response.meta['one_title']
        # 通过meta传递 获取到二级标题
        two_title = response.meta['two_title']
        # 返回三级标题的超链接
        a_list = response.xpath('//div[@class="filter-item"]/a')
        for a in a_list:
            # 通过二级标题的超链接 抓取到了三级标题的url和标题
            three_title = a.xpath('./text()').extract_first()
            # 抓取三级标题的url
            three_title_url = response.urljoin(a.xpath('./@href').extract_first())
            print(one_title, two_title, three_title, three_title_url)






"""
工程类
    一级工程
        建设工程经济
            1z101000
                1z101000时间金钱价值的计算
                    1.时间价值观念.txt
                    2.时间价值观念.txt
                    3.时间价值观念.txt
    二级工程
    ...
"""
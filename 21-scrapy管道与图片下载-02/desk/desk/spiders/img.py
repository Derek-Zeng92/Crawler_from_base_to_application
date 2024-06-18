import scrapy
from urllib.parse import urljoin

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['desk.zol.com.cn/dongman/']
    start_urls = ['http://desk.zol.com.cn/dongman/']

    def parse(self, response, **kwargs):
        # 抓取到每个详情页的url
        href_list = response.xpath('//ul[@class="pic-list2  clearfix"]/li/a/@href').extract()

        for href in href_list:
            # 取出不要的exe的url
            if href.find('exe') != -1:
                continue
            # 拼接url 获取到详情页的url
            detail_url = urljoin('http://desk.zol.com.cn/dongman/', href)
            # print(detail_url)
            # 请求详情页的url
            yield scrapy.Request(url=detail_url, callback=self.parse_detail)

    # 即系详情返回的响应对象
    def parse_detail(self, response):
        # 获取详情页中不同分辨率大小的图片的url
        detail_href = response.xpath('//dd[@id="tagfbl"]/a/@href').extract()
        # print(detail_href)
        if len(detail_href) > 1:
            # 继续拼接大图的url
            max_img_url = urljoin('http://desk.zol.com.cn/dongman/', detail_href[0])
            # print(max_img_url)
            # 请求大图页的url
            yield scrapy.Request(url=max_img_url, callback=self.parse_max_img)

    # 最后解析大图的url地址
    def parse_max_img(self, response):
        # 解析出最终大图的url
        url = response.xpath('//img[1]/@src').extract_first()
        print(url)
        yield {'img_src': url}
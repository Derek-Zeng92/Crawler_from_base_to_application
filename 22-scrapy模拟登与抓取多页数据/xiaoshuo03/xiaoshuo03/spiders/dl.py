import scrapy


class DlSpider(scrapy.Spider):
    name = 'dl'
    allowed_domains = ['17k.com']
    start_urls = ['https://user.17k.com/ck/user/myInfo/96139098?bindInfo=1&appKey=2406394919']


    def start_requests(self):
        login_url = 'https://passport.17k.com/ck/user/login'
        # 发送post、请求
        # yield scrapy.Request(login_url,method='POST',body='loginName=17346570232&password=xlg17346570232', callback=self.do_login)
        form_data = {
            'loginName': '17346570232',
            'password': 'xlg17346570232'
        }
        # 发送post请求
        yield scrapy.FormRequest(login_url, formdata=form_data, callback=self.do_login)


    def do_login(self, response):
        # print(response.text)
        # 登陆成功以后  请求登录后才能访问的url网址
        for url in self.start_urls:
            yield scrapy.Request(url)

    def parse(self, response, **kwargs):
        print(response.text)

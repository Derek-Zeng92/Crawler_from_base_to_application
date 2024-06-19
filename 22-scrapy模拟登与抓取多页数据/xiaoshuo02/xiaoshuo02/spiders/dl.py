import scrapy


class DlSpider(scrapy.Spider):
    name = 'dl'
    allowed_domains = ['17k.com']
    start_urls = ['https://user.17k.com/ck/user/myInfo/96139098?bindInfo=1&appKey=2406394919']

    def start_requests(self):
        # cookies字符串
        cookies = 'acw_tc=2760828b17187669188055278ea086cf2ee52e47cbd3c9c1197d0b04b307a1; GUID=50277ed9-4fe7-410c-a85a-6d9ebc074670; acw_sc__v2=66724d473954ad398f73d19d8c41faca0745a463; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1718766920; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F98%252F90%252F96139098.jpg-88x88%253Fv%253D1650527904000%26id%3D96139098%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BqYx51ZhI1%26e%3D1734319109%26s%3D451a057538a89d4b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296139098%22%2C%22%24device_id%22%3A%221902e7ddf9d8c2-036727f15d1699-26001c51-2073600-1902e7ddf9e947%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2250277ed9-4fe7-410c-a85a-6d9ebc074670%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1718767487; ssxmod_itna=eqRhqIxh8i4xzxAOD5GkKDCUDkUb81DRGx6AOx0y04eGzDAxn40iDtx=54DqnYXrdB2rc0YPDR+YNFeWz7GfI/Kxx0aDbqGkYjI4iiyDCeDIDWeDiDG4Gm94GtDpxG=Djm/ZCSLxYPGWRqDgR4GgldiD0bUnKTiD4qDB+odDKLi9BxDlBETzYDQoYYiDY3dxpLbBiGnxKY=DjLiD/8hOgo6YEcFz0wWF1ZNaKqGyYKGuAw2yfeDH7TXS/M5oWOeoGAfWFGPe9GDoBxht0zDoSiq+YgqYiGvxS7Y=nGDdjX4zDDfPjR3oeD==; ssxmod_itna2=eqRhqIxh8i4xzxAOD5GkKDCUDkUb81DRGx6AxnFSDDQqbDl=nc4j4+96dljZZYe/DSqidqjrYIms99ekWThrNIe8u4HyPqruP86cxlTmkrFZbjfyiQi1n1sdf294k8WumgYpPw/HA+S338BbqIeQqvSBqUKBjUAixqWM+dUqoe8g=QjOmFSAU=d8hiqOrc80K3C3=bueoQzLL5k=aS9DaxoAtkTe5srY38PTiTZ6DjC=y7dtxvCfXxYnoO33n1FKd2ilR=IzIUtSbl4RKVALCSejdle/Cel9=e41ySBSR+mG0rB+HZO+7AygmiDg+B9y1BR=nHjCuYf5q4qWinDXi3D07WBq6iKU0ocb4HBKkCmznhYrmM78D7=DY9IK04mr5204Kh5oGKeD; tfstk=fa8wrw4JmV3ZPNxcL9_VUicfzoQO7aH7uE6fiIAc1OXg5PwDYs1R5iDO5EJFWet_lOMOuIv5uYMSP4O96NQmFYtVGv8Crs5Gs-60KBV5ijjrP4O9sJb0aVuSMibCntBcoGjc-BXdgRXDnGq3K9CAiRf0SXRhpsbcst4gxBfPZtf0jbvWsI4FNGckVAK0VbNhoTAGICO9-Tw5UCfburSf_GrDs9z0oe-pBd5dI0FCHN6961JxyPQG0nY1-FDnoaxJLESlzmGOrFdD2nALQjWMOdLPSUka56sVQHYGYS4DZCXFYnJZQlBMfpSRtMVqy695KCLMYjeHsL6NS6jIrbRhmHTO2FM37axJ1NtDEvZ1I35c4G2Atr9vkhy00GfdTTGEt-ZUW7wo-vI4DoIhy6WS11ZYDGfdTTGEToEAx_CFFf11.'
        # 需要注意的是 传递cookies类型为字典
        cookie_dict = {i.split('=')[0].strip(): i.split('=')[1].strip() for i in cookies.split(';')}
        # print(cookie_dict)

        for url in self.start_urls:
            yield scrapy.Request(url, cookies=cookie_dict)


    def parse(self, response, **kwargs):
        print(response.text)

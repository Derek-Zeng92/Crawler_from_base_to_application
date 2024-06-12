'''
抓取ip的文件
'''
import requests
from proxy_redis import ProxyRedis  # ip代理池中处理ip的类
from lxml import etree


# 抓取ip
def get_ip(url):
    # 实例化处理ip的类
    p_r = ProxyRedis()
    # 注意cookie有反扒失效时间很多需要替换
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Cookie':'https_waf_cookie=3865ea93-f2b6-4c1eb058b79fdbea76a7d75fefa422b4458b; Hm_lvt_f9e56acddd5155c92b9b5499ff966848=1718160355; https_ydclearance=d5886a123d95806232bc1a0e-d83b-4222-98c9-73a8c4a8d486-1718188896; Hm_lpvt_f9e56acddd5155c92b9b5499ff966848=1718181699'
    }
    res = requests.get(url, headers=headers)
    html = res.content.decode()  # 解码
    # with open('89.html', 'w', encoding='UTF-8') as f:
    #     f.write(html)
    # with open('89.html', 'r', encoding='UTF-8') as f:
    #     html = f.read()
    # print(html)

    # 实例化xpath对象
    tree = etree.HTML(html)
    # 匹配到ip和端口 并使用切片去除不要的标题数据
    ip_list = tree.xpath('//*[@class="layui-table"]/tbody/tr')
    print(ip_list)
    if len(ip_list) != 0:
        next_url='https://www.89ip.cn/'+tree.xpath('//*[@class="layui-laypage-next"]/@href')[0]
        get_ip(next_url)
    # 循环拼接端口和ip
    for tr in ip_list:
        td=tr.xpath('.//td/text()')
        ip = td[0].strip() + ':' +td[1].strip()
        # print(ip)
        p_r.zset_zadd(ip)  # ip添加到有序集合中


if __name__ == '__main__':
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    # }
    main_url = 'https://www.89ip.cn/index_1.html'
    # response_main = requests.get(main_url, headers=headers)
    # 获取服务器端响应的cookie
    # cookies = response_main.cookies
    # print(dict(cookies))
    get_ip(main_url)   # 运行测试
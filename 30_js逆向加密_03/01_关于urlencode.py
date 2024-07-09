"""
url的组成-> 统一资源定位符 。
协议://域名：端口/虚拟路径/虚拟路径/.../文件?参数名=参数值&参数名=参数值#锚
https://www.baidu.com:443/a/b/c/search?name=胡辣汤&疙瘩汤&age=19&address=山东

# 闹幺蛾子.
查询name=胡辣汤&疙瘩汤=哈哈哈的内容
为了防止这样的问题出现.在请求之前会对url进行编码.
胡 => 十六进制处理 => 数字前面加上% => %XX
"""

# from urllib.parse import urlencode, quote, quote_plus, unquote, unquote_plus
#
# # s = "http://www.baidu.com/"
# # params = {
# #     "name": "樵夫&age=18",
# #     "address": "beijing"
# # }
# # # p = urlencode(params)  # 了解即可.我们不用这个..
# # # print(p)
# # #
# # # s = s + "?" + p
# # # print(s)
# #
# # # import requests
# # # r = requests.get(s, params=params)  # requests会自动帮我们完成上述操作.
# # # print(r.request.url)
# #
# # # 有些情况下. 对于cookie的维护. 需要我们手动计算的.
# # # 手工去完成randomcodesign的加密工作. 加密完了之后得到一个字符串(有可能有特殊符号).,
# # # 这个字符串必须加到cookie中. 这个字符串在加入cookie之前. 必须进行urlencode
# # s = "abc///de++f=="
# # # %E4%BD%A0%E5%A5%BD%E5%95%8A.%20%E6%88%91%E5%8F%AB%E8%B5%9B%E5%88%A9%E4%BA%9A
# # print(quote(s))
# # print(quote_plus(s))
#
# print(unquote("https://search.kongfz.com/product_result/?key=%E9%98%BF%E6%8B%89%E8%95%BE&status=0&_stpmt=eyJzZWFyY2hfdHlwZSI6Imhpc3RvcnkifQ==&pagenum=1&ajaxdata=1&type=1&_=1668429030829"))

from urllib.parse import urljoin

base_url = "https://www.baidu.com/a/b"

# "https://www.baidu.com/a/c/d/index.html"
u1 = "c/d/index.html"  # ?  1. xxxxxx
# "https://www.baidu.com/c/d/index.html"
u2 = "/c/d/index.html"  # ? 2. xxxxx

u1 = urljoin(base_url, u1)
u2 = urljoin(base_url, u2)
print(u1)
print(u2)

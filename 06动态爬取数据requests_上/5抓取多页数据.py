import urllib.request
import urllib.parse
import json
# 拿到地址
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
# 获取到当前浏览器请求所携带的表单数据
formData = {
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': 1,
    'pageSize': 100,
}
# 对表单数据进行转码
formData = urllib.parse.urlencode(formData).encode('UTF-8')
# 发送post请求
request = urllib.request.Request(url, data=formData, headers=headers)
response = urllib.request.urlopen(request)
# 返回json数据 转换成字典
data = json.loads(response.read().decode('UTF-8'))
print(data['Table1'])
# for l in data['Table1']:
#     print(l)
import urllib.request

url = 'http://www.baidu.com'
# 进行请求
response = urllib.request.urlopen(url)
# print(response)
# 获取状态码
print(response.getcode())
# 获取URL
print(response.geturl())
# 获取请求头
print(response.getheaders())
# 读取响应
print(response.read().decode('UTF-8'))
# 下载数据 保存文件名称为baidu.html
urllib.request.urlretrieve(url, filename='baidu.html')

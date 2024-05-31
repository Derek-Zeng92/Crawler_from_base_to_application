import requests

url = 'http://www.baidu.com'
# 发起get请求
response = requests.get(url)
# print(response)
# 设置编码
# response.encoding = 'UTF-8'
# 打印一下响应内容
# print(response.text)

# 返回bytes
# print(response.content.decode('UTF-8'))

# 获取请求的url
# print(response.url)

# 获取状态码
# print(response.status_code)

# 获取响应对应的请求头
# print(response.request.headers)

# 目前记住 后期单讲关于cookie操作
# 获取响应的cookie
# print(response.cookies)

print(response.ok)
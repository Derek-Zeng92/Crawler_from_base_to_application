import urllib.request
url = 'https://www.baidu.com/s?wd=%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4'
# url转码
# print(urllib.request.unquote(url))
# url = urllib.request.unquote(url)
# print(url)
headers = {
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
# 构造请求对象
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
# with open('baidu.html', 'wb') as f:
#     f.write(response.read())
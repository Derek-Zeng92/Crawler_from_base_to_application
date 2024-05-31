import requests
url = 'https://www.baidu.com/s?'
# key_word = '迪丽热巴'
key_word = input('输入搜索内容：')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
data = {
    'wd': key_word
}
# 构造请求对象
response = requests.get(url, params=data, headers=headers)
with open('baidu.html', 'wb') as f:
    f.write(response.content)
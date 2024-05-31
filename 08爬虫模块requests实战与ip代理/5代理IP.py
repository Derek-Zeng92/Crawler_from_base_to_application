import requests

# 代理 ip
proxy = {
    'http': 'http://47.112.122.163:82'
}
"""
[{
    'http': 'http://47.112.122.163:82'
},{
    'http': 'http://47.112.122.163:82'
},{
    'http': 'http://47.112.122.163:82'
}]
"""
url = 'https://www.baidu.com/s?'

data = {
    'wd': 'IP查询'
}
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

# 建议使用代理  也要把反扒取得一些参数带上
response = requests.get(url, params=data, proxies=proxy, headers=headers)
response.encoding = 'UTF-8'
with open('ip.html', 'w', encoding='UTF-8') as f:
    f.write(response.text)
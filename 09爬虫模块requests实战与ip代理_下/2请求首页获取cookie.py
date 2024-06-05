import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
# 给一个
main_url = 'https://xueqiu.com/'
response_main = requests.get(main_url, headers=headers)
print(response_main)
# 获取服务器端响应的cookie
cookies = response_main.cookies
print(cookies)
print(dict(cookies))
# 异步加载数据的url
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=366242&size=15'
response = requests.get(url, headers=headers, cookies=cookies)
print(response)
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
# 先访问首页 获取到cookie
session = requests.Session()   # 创建一个session对象
main_url = 'https://xueqiu.com/'
# 这里请求的目的就一个 拿到响应的cookie
session.get(url=main_url, headers=headers)

# 访问异步加载的地址 携带着cookie过去
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=366242&size=15'
res = session.get(url, headers=headers)
print(res)
print(res.json())
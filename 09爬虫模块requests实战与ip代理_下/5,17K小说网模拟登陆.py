import requests

# 模拟登陆的入口
url = 'https://passport.17k.com/ck/user/login'
# 携带请求参数
data = {
    'loginName': '17346570232',
    'password': 'xlg17346570232',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
res = requests.post(url, data=data, headers=headers)
print(res)
cookies = dict(res.cookies)
# 登陆后才能访问的
url = 'https://user.17k.com/ck/user/myInfo/96139098?bindInfo=1&appKey=2406394919'
res = requests.get(url, headers=headers, cookies=cookies)
print(res)
print(res.text)
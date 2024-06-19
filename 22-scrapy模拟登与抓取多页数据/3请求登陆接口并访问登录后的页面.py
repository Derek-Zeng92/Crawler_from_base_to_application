import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
# 登陆接口的url
url = 'https://passport.17k.com/ck/user/login'
data = {
    'loginName': '17346570232',
    'password': 'xlg17346570232'
}
resp = requests.post(url, headers=headers, data=data)
# print(resp.text)
print(dict(resp.cookies))

# 登陆以后才能访问的url地址
url = 'https://user.17k.com/ck/user/myInfo/96139098?bindInfo=1&appKey=2406394919'
resp = requests.get(url, headers=headers, cookies=resp.cookies)
print(resp.json())
import requests
import base64
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def base64_api(img):
    data = {"username": 'q6035945', "password": 'q6035945', "typeid": 3, "image": img}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


session = requests.session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

# 1. 加载第一个请求
session.get("https://user.wangxiao.cn/login?url=http%3A%2F%2Fks.wangxiao.cn%2F")

# 2. 加载验证码图片
img_resp = session.post("https://user.wangxiao.cn/apis//common/getImageCaptcha",
                       headers={
                           "Content-Type": "application/json;charset=UTF-8"
                       })

img_json = img_resp.json()
img_base64 = img_json['data'].split(",")[1]

with open('tu.png', mode="wb") as f:
    f.write(base64.b64decode(img_base64))

# 识别图片
verify_code = base64_api(img_base64)
print(verify_code)


# getTime -> 返回的东西(一个时间戳) ->  和密码一起加密

# 3. 请求getTime
time_url = "https://user.wangxiao.cn/apis//common/getTime"
time_resp = session.post(time_url, headers={
                           "Content-Type": "application/json;charset=UTF-8"
                       })
tm = time_resp.json()['data']
print(tm)

# 4. 准备对密码进行加密

username = "18614075987"
password = "q6035945"

pub_key_str = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"

pub_key = RSA.import_key(base64.b64decode(pub_key_str))
rsa = PKCS1_v1_5.new(key=pub_key)
password_bs = rsa.encrypt((password + str(tm)).encode("utf-8"))

password_b64 = base64.b64encode(password_bs).decode()

login_url = "https://user.wangxiao.cn/apis//login/passwordLogin"
data = {
    "imageCaptchaCode": verify_code,
    "password": password_b64,
    "userName": username,
}

login_resp = session.post(url=login_url, data=json.dumps(data),
                          headers={
                              "Content-Type": "application/json;charset=UTF-8"
                          })

# print(login_resp.text)
login_info = login_resp.json()['data']
# 按照浏览器上的js的后续逻辑. 把cookie补齐. 才可以继续请求.....
print(session.cookies)
# 登陆成功

session.cookies['autoLogin'] = "true"
session.cookies['userInfo'] = json.dumps(login_info)
session.cookies['token'] = login_info['token']

session.cookies['UserCookieName'] = login_info['userName']
session.cookies['OldUsername2'] = login_info['userNameCookies']
session.cookies['OldUsername'] = login_info['userNameCookies']
session.cookies['OldPassword'] = login_info['passwordCookies']
session.cookies['UserCookieName_'] = login_info['userName']
session.cookies['OldUsername2_'] = login_info['userNameCookies']
session.cookies['OldUsername_'] = login_info['userNameCookies']
session.cookies['OldPassword_'] = login_info['passwordCookies']

session.cookies[login_info['userName'] + "_exam"] = login_info['sign']

# 5. 验证登陆是否成功. session是否可用
list_questions_url = "http://ks.wangxiao.cn/practice/listQuestions"
data = {"practiceType":"2","sign":"jz1","subsign":"8cc80ffb9a4a5c114953","examPointType":"","questionType":"","top":"30"}
resp = session.post(list_questions_url, data=json.dumps(data),
             headers={
                 "Content-Type": "application/json;charset=UTF-8"
             })
print(resp.json())  # 能够得到json数据. 证明登陆是ok的.

# 禁止用协程干这个网站....

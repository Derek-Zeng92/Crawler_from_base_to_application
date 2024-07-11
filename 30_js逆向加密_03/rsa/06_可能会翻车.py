import requests
import json
import time
from hashlib import md5


url = "https://www.hengyirong.com/api/v1/user/login"
# key的存储是hash表(无序的)
data = {
    "password":"123456",
    "sms_login":0,
    "username":"1653123154",
}
headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "aliyungf_tc=cd4ef5988e573fdaf550b99d29199ed22bd00bb9bd22b9e6aa3fa619ac924628",
    "Referer": "https://www.hengyirong.com/user/login/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "x-access-token":"",
    "x-appid": "pc",
    "x-client-info": "pc",
    "x-client-version": "1.2.0",
    "x-v": "1.0.0",
    "x-ver": "1.1"
}


data_final = json.dumps(data, separators=(',', ':'))

# 想办法计算x-t, x-sign
f = int(time.time())
# 把参数进行处理. json字符串. 接下来是巨大的坑....
s = '/v1/user/login|1.0.0|pc|DHz@uEun&k^LtqbhYqUN5wetfaO8p2|'+str(f)+'||pc|1.2.0|'+data_final
obj = md5()
obj.update(s.encode())
s = obj.hexdigest()

headers['x-sign'] = s
headers['x-t'] = str(f)
print(f)

# json.dumps(data, separators=(',', ':')) 比replace好.
resp = requests.post(url, data=data_final, headers=headers)
print(resp.json())

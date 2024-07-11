import execjs
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import binascii
import json


def a(i):
    b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.sample(b, i))


def b(s, k):
    aes = AES.new(key=k.encode("utf-8"), mode=AES.MODE_CBC, IV=b'0102030405060708')
    s = s.encode("utf-8")
    s = pad(s, 16)
    bs = aes.encrypt(s)
    return base64.b64encode(bs).decode()


def c(s, n, e):
    s = s[::-1]  # 需要翻转
    s = int(binascii.b2a_hex(s.encode()).decode(), 16)
    n = int(n, 16)
    e = int(e, 16)
    # 0xfffffff
    return hex(s ** e % n).replace("0x", "")


def encrypt(s):
    g = "0CoJUm6Qyw8W8jud"
    f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    e = "010001"

    h = {}
    i = a(16)
    h['encText'] = b(s, g)
    h['params'] = b(h['encText'], i)
    h['encSecKey'] = c(i, f, e)
    return h


if __name__ == '__main__':

    data = {
        "ids": [1325905146],
        "level": "standard",
        "encodeType": "aac",
        "csrf_token": ""
    }

    data = encrypt(json.dumps(data))
    # print(data)

    import requests
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    resp = requests.post(url="https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=", data=data, headers=headers)
    # 用resp.json()不好用的时候。 换json.loads() , 如果json.loads() 也不好用. 你会怎么办?
    # print(json.loads(resp.text))
    resp_s = resp.text

    js = execjs.compile(r"function fn(s){return JSON.parse(s+'')}")  # 在js里一定可用...
    dic = js.call("fn", resp_s)
    print(dic)

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs


import requests

session = requests.session()
session.headers[
    "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

# 1. 加载cookie
first_url = "https://www.qimai.cn/rank"

session.get(first_url)

get_data_url = "https://api.qimai.cn/rank/index"
params = {
    "brand": "free",
    "device": "iphone",
    "country": "cn",
    "genre": "36",
}
# 计算ana>>>>

js = execjs.compile(open("某麦分析.js", mode="r", encoding="utf-8").read())
new_url = js.call("get_mm", get_data_url, params)

session.cookies['qm_check'] = "A1sdRUIQChtxen8tJ0NMMRcOUFseEHBeQF0NSjFNWCwycRd1QlhAXFECEUNTT0lacV5AVVpEB3xQU0MSCyZPagcSQEpvAWdRTkMgSz1LBB4QHBtTXF0CCUFeWklWBRsCHAkcBBoc";

data_resp = session.get(new_url, params=params)
print(data_resp.json())

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

aes = AES.new(key=b'fX@VyCQVvpdj8RCa', IV=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', mode=AES.MODE_CBC)

bs = 'f98d13f3e4f16624a96e079b8eee0ffe'.encode()
print(len(bs))  # 32
bs = pad(bs, 16)  # 我忽略了一个事情. 被加密的内容长度刚好是16的倍数, 而在AES的填充过程中. 如果是刚好16的倍数. 需要在末尾增加16个填充
r = aes.encrypt(bs)
print(base64.b64encode(r).decode())

# "OsUc2B/X6sQ9kyq0HuSKerq/GkSMezien80Diu41WJVVwahABGc0XVWZK2dlj5+3"
# "OsUc2B/X6sQ9kyq0HuSKerq/GkSMezien80Diu41WJVVwahABGc0XVWZK2dlj5+3"
print(len(r))

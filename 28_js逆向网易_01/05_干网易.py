# 需要找到 https://music.163.com/weapi/comment/resource/comments/get    ?csrf_token=
#                            /weapi/song/enhance/player/url/v1
# 参数: params, 经过2次AES加密得到的
#      encSecKey 经过1次RSA加密得到的.
# 知道
# 原始数据

# 参数
"""
params: SRODdPJ5AshyZtoDvyvTTQwzZLusjveVmKSFBnzKJ3SFJCAIdp6zIQVVWmsgwFv5QajsK6vLlndKmLK8BfH77ErDCX8TOklGkPXT4kQ4YJ5yp6DBcaoFhgWgqsQLIgf1xuAx3KjCM1sy9x5D4x8r5SGWegXWCjOhGLGkAOPm+wIrNvyjUOVSPGzQrYUHP00bOituJIBaDrSB1NnCfy7W4Gw7Y5QfnU4//cbmTFgYyouV/X8pqMsI8KbYlxeVrX5t3vYmVH2knypCLBLsS/08nQtfqpy2pG8V1FASv5haaFk=
encSecKey: 392a898b55e413b70defd797fb00e20f16bb092244548d3c4fd271c9f4e8db627817d600b625b24c7881d20c6d06b06b4e2a2eedcde7557c096d5bcc52007f36911180d46791f05675da1c644795dae9366dd026819ca657545af9c37b5c25c3b616dcc9b2468c1aa839e81484f69d5e9559be1fb86c9e804fa1135a2f4290ee
"""

"""
rid=R_SO_4_2604592456
threadId=R_SO_4_2604592456
pageNo=2
pageSize=20
cursor=1720164211933
offset=0
orderType=1
"""

from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs
import json
data = {
    "ids": f"[{input('请输入一个歌曲的id:')}]",  # 输入歌曲的id  "[歌曲id]"
    "level": "standard",
    "encodeType": "aac",
    "csrf_token": ""
}

s = json.dumps(data)

js = execjs.compile(open("wy加密.js",mode="r", encoding="utf-8").read())
print(s)
dic = js.call("fn", s)
print(dic)

real_data = {
    "params": dic['encText'],
    "encSecKey": dic['encSecKey']
}

import requests

url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
resp = requests.post(url, data=real_data, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})

print(resp.text)

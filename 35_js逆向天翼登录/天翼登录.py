import requests
import time
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs

comParam_curTime = time.time() * 1000 - 1458
comParam_seqCode = ''
comParam_signature = ''
userName = 'asdfsaf@163.com000000000'
pwd = '123456'
password = ''

with open('ty.js', mode='r', encoding='utf-8') as f:
    tyjs = execjs.compile(f.read())
    headerParams = tyjs.call('fn')
    loginParams = tyjs.call('login', userName, pwd)
    comParam_curTime = headerParams['comParam_curTime']
    comParam_seqCode = headerParams['comParam_seqCode']
    comParam_signature = headerParams['comParam_signature']
    password = loginParams

url = f'https://m.ctyun.cn/account/login?referrer=wap&mainVersion=300031500&comParam_curTime=${comParam_curTime}&comParam_seqCode=${comParam_seqCode}&comParam_signature=${comParam_signature}&isCheck=true&locale=zh-cn'

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}

data = {
    'userName': userName,
    'password': password
}

resp = requests.post(url, data=data, headers=headers)
print(resp.text)

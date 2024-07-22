import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
f = open("第一个w.js", mode="r", encoding="utf-8")
first_js = execjs.compile(f.read())

f = open("第二个w.js", mode="r", encoding="utf-8")
second_js = execjs.compile(f.read())

import requests
import time
import re
import json



def get_now():
    return int(time.time() * 1000)

def jsonp_handle(text):
    jsonp_re = re.compile(r"\((?P<code>.*)\)", re.S)
    jsonp_str = jsonp_re.search(text, re.S).group("code")
    return json.loads(jsonp_str)


session = requests.session()
session.headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

# ============第一次请求, 注册验证码===================

regist_url = f"https://www.geetest.com/demo/gt/register-slide?t={get_now()}"
regist_resp = session.get(regist_url)
regist_dict = regist_resp.json()
gt = regist_dict['gt']
challenge = regist_dict['challenge']

# ============第二次请求. 访问gettype =================
get_type_url = "https://apiv6.geetest.com/gettype.php"
get_type_params = {
    "gt": gt,
    "callback": f"geetest_{get_now()}"
}

get_type_resp = session.get(get_type_url, params=get_type_params)
# print(get_type_resp.text)

# ================第三次请求, 访问第一波get.php ======================
first_get_url = "https://apiv6.geetest.com/get.php"

first_get_dict = first_js.call("cul_first_w", gt, challenge)

# 获取第一次计算之后的aeskey
aeskey = first_get_dict['aeskey']
finger_print = first_get_dict['finger_print']

first_get_params = first_get_dict['msg']
first_get_params['callback'] = f"geetest_{get_now()}"

first_get_resp = session.get(first_get_url, params=first_get_params)
first_get_resp_dict = jsonp_handle(first_get_resp.text)

s = first_get_resp_dict.get("data").get('s')

# 第一次发送请求到https://api.geetest.com/ajax.php

second_w = second_js.call('cul_second_w', aeskey, gt, challenge, s, finger_print)

first_ajax_url = "https://api.geetest.com/ajax.php"
first_ajax_params = {
    "gt": gt,
    "challenge": challenge,
    "lang": "zh-cn",
    "pt": 0,
    "client_type": "web",
    "w": second_w,
    "callback": f"geetest_{get_now()}"
}

first_ajax_resp = session.get(first_ajax_url, params=first_ajax_params)
print('获取图片：',first_ajax_resp.text)

# 第二次发送get.php
second_get_url = "https://api.geetest.com/get.php"
second_get_params = {
    "is_next": "true",
    "type": "slide3",
    "gt": gt,
    "challenge": challenge,
    "lang": "zh-cn",
    "https": "true",
    "protocol": "https://",
    "offline": "false",
    "product": "popup",
    "api_server": "api.geetest.com",
    "isPC": "true",
    "autoReset": "true",
    "width": "100%",
    "callback": f"geetest_{get_now()}",
}

second_get_resp = session.get(second_get_url, params=second_get_params)
second_get_dict = jsonp_handle(second_get_resp.text)

print(second_get_dict)
print('gt和challenge：',gt, challenge)

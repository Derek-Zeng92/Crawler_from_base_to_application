from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs
import requests


js = execjs.compile(open("抠js.js", mode="r", encoding="utf-8").read())

word = input("请输入你要翻译的单词:")
r = js.call("fn", word)
print(r)  # 加密的东西搞定了.

form_data = {
    "i": word,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",

    "salt":  r["salt"],
    "sign": r["sign"],
    "lts": r["ts"],
    "bv": r["bv"],

    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
}

url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
    "Cookie": "OUTFOX_SEARCH_USER_ID=-922898077@10.110.96.160; _ga=GA1.2.50793062.1656497331; OUTFOX_SEARCH_USER_ID_NCOO=1490949463.084894; ___rl__test__cookies=1668004707920",
    "Referer": "https://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
resp = requests.post(url, data=form_data, headers=headers)
print(resp.text)

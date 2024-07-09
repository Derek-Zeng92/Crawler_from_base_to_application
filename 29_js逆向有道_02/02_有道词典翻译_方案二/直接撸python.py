from hashlib import md5
import time


def my_md5(s: str):  # s我计划是str
    obj = md5()
    obj.update(s.encode("utf-8"))
    return obj.hexdigest()


t = my_md5('5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
r = str(int(time.time() * 1000))
i = r + "8"

word = input("给老师一个单词:")

dic = {
    "ts": r,
    "bv": t,
    "salt": i,
    "sign": my_md5("fanyideskweb" + word + i + "Ygy_4c=r#e#4EX^NUGUc5")
}

form_data = {
    "i": word,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",

    "salt":  dic["salt"],
    "sign": dic["sign"],
    "lts": dic["ts"],
    "bv": dic["bv"],

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

import requests
resp = requests.post(url, data=form_data, headers=headers)
print(resp.text)

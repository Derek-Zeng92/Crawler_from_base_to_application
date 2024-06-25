# encoding:utf-8
import re
import json
import requests

url = "https://floor.jd.com/recommend-v20/market_bill/get?source=pc_home&except_item_id=7957&pin=&uuid=16571764788271195153778&area=1_2802_0_0&callback=jsonpMarket&_=1666019411149"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)

obj = re.compile(r"\((?P<name>.*)\)", re.S)
r = obj.search(resp.text).group("name")
dic = json.loads(r)
print(type(dic))

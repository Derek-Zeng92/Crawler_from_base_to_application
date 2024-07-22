import re
import json

import requests

res = requests.get("https://www.bilibili.com/video/BV1ne4y1H7Zk/")
data_list = re.findall(r'__INITIAL_STATE__=(.+);\(function', res.text)
data_dict = json.loads(data_list[0])

aid = data_dict['aid']
cid = data_dict['videoData']['cid']

print(aid)
print(cid)

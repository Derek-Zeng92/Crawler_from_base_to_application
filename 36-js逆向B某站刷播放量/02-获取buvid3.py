import re
import json

import requests

res = requests.get("https://www.bilibili.com/video/BV1ne4y1H7Zk/")

cookie_dict = res.cookies.get_dict()

print(cookie_dict)

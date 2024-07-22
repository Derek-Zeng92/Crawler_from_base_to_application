import math
import random
import time
import uuid
import requests
import re
import json


def gen_uuid():
    uuid_sec = str(uuid.uuid4())
    time_sec = str(int(time.time() * 1000 % 1e5))
    time_sec = time_sec.rjust(5, "0")

    return "{}{}infoc".format(uuid_sec, time_sec)


def gen_b_lsid():
    data = ""
    for i in range(8):
        v1 = math.ceil(16 * random.uniform(0, 1))
        v2 = hex(v1)[2:].upper()
        data += v2
    result = data.rjust(8, "0")

    e = int(time.time() * 1000)
    t = hex(e)[2:].upper()

    b_lsid = "{}_{}".format(result, t)
    return b_lsid


video_url = "https://www.bilibili.com/video/BV1Pi4y1D7uJ"
bvid = video_url.rsplit("/")[-1]
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
})

res = session.get(video_url)
data_list = re.findall(r'__INITIAL_STATE__=(.+);\(function', res.text)
data_dict = json.loads(data_list[0])
aid = data_dict['aid']
cid = data_dict['videoData']['cid']

_uuid = gen_uuid()
session.cookies.set('_uuid', _uuid)

b_lsid = gen_b_lsid()
session.cookies.set('b_lsid', b_lsid)

session.cookies.set("CURRENT_FNVAL", "4048")

res = session.get("https://api.bilibili.com/x/frontend/finger/spi")
buvid4 = res.json()['data']['b_4']

session.cookies.set("CURRENT_BLACKGAP", "0")
session.cookies.set("blackside_state", "0")

res = session.get(
    url='https://api.bilibili.com/x/player/v2',
    params={
        "cid": cid,
        "aid": aid,
        "bvid": bvid,
    }
)

print(res.cookies.get_dict())

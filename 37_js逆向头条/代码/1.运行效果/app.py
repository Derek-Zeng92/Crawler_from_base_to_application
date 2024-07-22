import time

import requests
import execjs
import os

os.environ["NODE_PATH"] = "/usr/local/lib/node_modules/"
with open('sdk.js', mode='r', encoding='utf-8') as f:
    js = f.read()
JS = execjs.compile(js)

min_behot_time = 1664884732
cookie_dict = {}
while True:
    print(min_behot_time)
    url = "https://www.toutiao.com/api/pc/list/feed?channel_id=3189398999&max_behot_time={}&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web".format(
        min_behot_time)

    signature = JS.call("get_sign", url)
    final_url = f"{url}&_signature={signature}"

    res = requests.get(
        url=final_url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            # "referer": "https://www.toutiao.com/?wid=1664893444672"
        },
        cookies=cookie_dict
    )

    # print(res.text)
    cookie_dict.update(res.cookies.get_dict())
    data_dict = res.json()
    print(data_dict['has_more'])
    for item in data_dict['data']:
        print(item['behot_time'], item['title'][0:10])
        min_behot_time = item['behot_time']
    res.close()

    time.sleep(5)

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs

from lxml import etree

import requests
import json
import re

#
# 负责组装好session
def init():
    session = requests.session()

    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    # 整体逻辑应该是:
    # 1.拿页面源代码. 提取到"开了门.js"的下载地址
    # 2. 访问"开了门.js"的下载地址, 获取到js内容. 提取到TOKEN_SERVER_TIME
    # 3. 把TOKEN_SERVER_TIME怼到你的js代码里.

    page_resp = session.get("http://iwencai.com/unifiedwap/home/index")
    page_html = page_resp.text

    tree = etree.HTML(page_html)
    src = tree.xpath("//script[1]/@src")[0]
    src = "http:" + src


    js_response = session.get(src)
    kailemen_js_code = js_response.text
    server_time_re = re.compile(r"var TOKEN_SERVER_TIME=(?P<kailemen_server_time>.*?);")
    kailemen_server_time = server_time_re.search(kailemen_js_code).group('kailemen_server_time')
    print(kailemen_server_time)


    f = open("问财抠.js", mode="r", encoding="utf-8")
    js_content = f.read()
    # 把缺少的TOKEN_SERVER_TIME补充进去
    js_content = "var TOKEN_SERVER_TIME = " + str(kailemen_server_time) +";\n" + js_content
    js = execjs.compile(js_content)

    # 在访问之前. 加上v??
    v = js.call("fn")
    session.cookies['v'] = v
    return session


def work(msg):
    global session
    robot_url = 'http://iwencai.com/customized/chart/get-robot-data'
    data = {
        "question": msg,
        "perpage": 50,
        "page": 1,
        "secondary_intent": "stock",
        "log_info": {
            "input_type": "click"
        },
        "source": "Ths_iwencai_Xuangu",
        "version": "2.0",
        "query_area": "",
        "block_list": "",
        "add_info": {
            "urp":
                {
                    "scene": 1,
                    "company": 1,
                    "business": 1
                },
            "contentType": "json",
            "searchInfo": True
        },
        "rsh": "Ths_iwencai_Xuangu_oj75gnxggqs8xps6lf2paqy8qtf2ag50"
    }
    while 1:
        try:
            resp = session.post(robot_url, data=json.dumps(data, separators=(",", ":")), headers={
                "Content-Type": "application/json"
            })
            return resp.json()
        except Exception as e:
            print("报错了,,,",e)
            session = init()


session = init()

import os
from datetime import datetime

# 获取当前日期和时间
now = datetime.now()
def write_to_log(log_string):
    # 检测是否存在 log 文件夹，如果不存在则创建
    if not os.path.exists('log'):
        os.makedirs('log')

    # 定义日志文件路径
    log_file_path = os.path.join('log', 'log.txt')

    # 打开文件并写入字符串
    with open(log_file_path, 'a') as file:
        file.write(log_string + '\n')

log_message = work("今日连板")
print(str(now)+str(log_message))
write_to_log(str(now)+str(log_message))
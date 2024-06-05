import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import json


driver = Chrome()
driver.get('https://so.gushiwen.cn/user/collect.aspx')

with open('gsw_cookie.text', 'r', encoding='UTF-8') as f:
    listCookies = json.loads(f.read())

for cookies in listCookies:
    # print(cookies)
    cookie_dict = {}
    for k,v in cookies.items():
        cookie_dict[k] = v
    # 添加cookie到selenium
    driver.add_cookie(cookie_dict)
driver.refresh()  # 刷新页面
driver.get('https://so.gushiwen.cn/user/collect.aspx')  # 在重新访问一遍

time.sleep(100)
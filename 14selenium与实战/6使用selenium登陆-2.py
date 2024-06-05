import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import base64
import json
import requests

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

driver = Chrome()
driver.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')

# 查找用户名节点
driver.find_element(By.ID, 'email').send_keys('793390457@qq.com')
# 查找密码节点
driver.find_element(By.ID, 'pwd').send_keys('xlg17346570232')
# 查找验证码的图片节点
imageCode = driver.find_element(By.ID, 'imgCode')
# 截图  截取imageCode节点的截图（验证码）
imageCode.screenshot('yzm.png')
img_path = "./yzm.png"
result = base64_api(uname='luckyboyxlg', pwd='17346570232', img=img_path, typeid=3)
print(result)
# 查找验证码节点
driver.find_element(By.ID, 'code').send_keys(result)

# 查找登陆按钮节点
denglu = driver.find_element(By.ID, 'denglu')
denglu.click()
time.sleep(100)
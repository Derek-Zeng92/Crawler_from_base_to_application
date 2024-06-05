import time
from selenium.webdriver import Chrome


# 实例化
driver = Chrome()
# 访问百度
driver.get('http://www.baidu.com')
print(driver.title)
# 阻塞
time.sleep(100)
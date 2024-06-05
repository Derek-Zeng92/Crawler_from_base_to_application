import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.implicitly_wait(10)
driver.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')
driver.maximize_window()  #最大化浏览器窗口
# 查找用户名节点
driver.find_element(By.ID, 'email').send_keys('793390457@qq.com')
# 查找密码节点
driver.find_element(By.ID, 'pwd').send_keys('xlg17346570232')
# 查找验证码的图片节点
imageCode = driver.find_element(By.ID, 'imgCode')
# 截图  截取imageCode节点的截图（验证码）
imageCode.screenshot('yzm.png')
# 查找验证码节点
driver.find_element(By.ID, 'code')

# 查找登陆按钮节点
denglu = driver.find_element(By.ID, 'denglu')

time.sleep(100)
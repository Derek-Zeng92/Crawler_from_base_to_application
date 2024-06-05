import time

from selenium.webdriver import Chrome

driver = Chrome()
driver.get('https://www.linovelib.com/novel/2547/123015.html')
# 获取页面源代码
data = driver.page_source
print(data)
time.sleep(1000)
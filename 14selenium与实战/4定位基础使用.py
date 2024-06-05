import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver = Chrome()
driver.get('https://www.gushiwen.cn/')
# By.ID 右上角的搜索框
txtKey = driver.find_element(By.ID, 'txtKey')
# txtKey = driver.find_element_by_id('txtKey')  # 老版本的可以用 但是不建议  现在最新版本已经无法使用
txtKey.send_keys('唐诗')  # 像input输入框输入搜索内容
# 找到点击搜索的按钮
search = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/form/input[3]')
search.click()  # 点击搜索按钮
# print(txtKey)
# 给一个不存在的匹配的节点  报错
# txtKey = driver.find_element(By.ID, 'xxxx')

# 获取所有的超链接a
# a = driver.find_elements(By.TAG_NAME, 'a')
# for url in a:
    # print(url)
    # print(url.get_attribute('href'))

# find_elements给一个不存在的节点  xxxx  返回空列表 不报错
# a = driver.find_elements(By.TAG_NAME, 'xxxxx')
# print(a)

# 右侧的搜索框
# txtKey = driver.find_element(By.XPATH, '//*[@id="txtKey"]')
# txtKey.send_keys('唐诗')

# 错误写法
# txtKey = driver.find_element(By.XPATH, '//*[@id="txtKey"]/text()')


# txtKey = driver.find_elements(By.CLASS_NAME, 'cont')
# print(txtKey)
# for i in txtKey:
#     print(i.text)  # 获取节点中的文本内容
# 获取页面内容
print(driver.page_source)
time.sleep(100)









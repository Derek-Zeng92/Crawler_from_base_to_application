from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument("--headless")
opt.add_argument('--disable-gpu')

web = Chrome(options=opt)
web.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')

print(web.page_source)
time.sleep(100)
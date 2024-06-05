from urllib.parse import urljoin
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
session = requests.Session()
session.get('https://www.9meiju.cc/', headers=headers)
# 请求电影网址
url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-1.html'
resp = session.get(url, headers=headers)
resp.encoding = 'UTF-8'
data = resp.text
with open('电影.html', 'w', encoding='UTF-8') as f:
    f.write(data)

with open('电影.html', 'r', encoding='UTF-8') as f:
    data = f.read()

first_m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')

# 请求第一次m3u8de url
resp = session.get(first_m3u8_url, headers=headers)
with open('first_m3u8_url.text', 'wb') as f:
    f.write(resp.content)
resp.encoding = 'UTF-8'
print(resp.text)


with open('first_m3u8_url.text', 'r', encoding='UTF-8') as f:
    data = f.read()

# 第二次请求m3u8文件地址 返回最终包含所有ts文件的m3u8
second_m3u8_url = urljoin(first_m3u8_url, data.split('/', 3)[-1].strip())
resp = session.get(second_m3u8_url, headers=headers)
with open('second_m3u8_url.text', 'wb') as f:
    f.write(resp.content)

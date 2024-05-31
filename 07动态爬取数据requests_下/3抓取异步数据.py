import requests

# 抓取异步数据
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
response = requests.get(url, headers=headers)
print(response)
# print(response.json())
subjects = response.json()['subjects']
for i in subjects:
    print(i)

# 将封面进行下载
# 使用request和urllib进行下载
# 根据当前电影 抓取详情页
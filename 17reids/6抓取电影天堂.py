import redis
from lxml import etree
import requests
# r = redis.StrictRedis(host='127.0.0.1', port=6379, password='123456', decode_responses=True)
r = redis.StrictRedis(password='123456', decode_responses=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
res = requests.get(url, headers=headers)
tree = etree.HTML(res.content.decode('GBK'))
title = tree.xpath('//div[@class="co_content8"]/ul//a/text()')
con = tree.xpath('//div[@class="co_content8"]/ul//tr[4]/td/text()')
# print(con)
# 存储到redis中的列表（队列）
r.rpush('ddtt8', ''.join(title)+"|"+''.join(con))
# 从redis中获取
print(r.lrange('ddtt8', 0, -1))
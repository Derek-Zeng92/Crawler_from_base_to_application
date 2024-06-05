import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Host': 'xueqiu.com',
    'Referer': 'https://xueqiu.com/',
    'Cookie': 'acw_tc=2760827f16563325199711002e84d24a3fcaa8c8aa29c92f5dd41704624d0d; xq_a_token=71618bed86fb8c37819bc7e19fe00d51ec2386f8; xqat=71618bed86fb8c37819bc7e19fe00d51ec2386f8; xq_r_token=88812666b17c6dc5f6bdbf432fda4b49b23f7924; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY1NzkyNzc0MywiY3RtIjoxNjU2MzMyNDg5ODI4LCJjaWQiOiJkOWQwbjRBWnVwIn0.KEvHRgjIdLGeZEhHI_IxfjZ5_gr3VyW-GZPYXphtf0IQULOOHcj63lT4WTUf1nP9yA03HBvRBWEzROzV8E8klcFLht1DViRuW6h2vpyLdiCjmH6xZyGIXlpZat9Z-8HT4JTNU1u-0ZTCxOeIDrS1dhjpJe6Vq3DvHuhNhlBmYGFLDaEBwqdSzv7FKL_3bf2iVItRFfGKUZjn8pHTP4Yj6QGsKiTNovc81SHFhSOb11nPxfT9NTAhtcesvwayaPqmSiFu__2f9ax6k82e1lP1qMI3KoQF2p0ubhHJdwYD7iYkW6wzRhR-kkzizSbdzktxIyyAyWHWWyH6iWXhAg35uQ; u=381656332519979; device_id=04df9bee31d96920289fbec1a4e1e03a; Hm_lvt_1db88642e346389874251b5a1eded6e3=1656332522; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1656332545',
}
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=366242&size=15'

response = requests.get(url, headers=headers)
print(response.json())

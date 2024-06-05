import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

res = requests.get('https://www.linovelib.com/novel/2547/123015.html', headers=headers)
data = res.content.decode('UTF-8')
with open('book.html', 'w', encoding='UTF-8') as f:
    f.write(data)

print(data)
import requests

url = 'https://www.baidu.com/img/bd_logo1.png'

response = requests.get(url)
# print(response.ok)
# print(response.content)
with open('baidu.jpg', 'wb') as f:
    f.write(response.content)
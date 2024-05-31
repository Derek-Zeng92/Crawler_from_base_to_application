import requests
import json
url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=e8e4138da7331251'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
# 表单提交给服务器的数据
form_data = {
    'from': 'en',
    'to': 'zh',
    'q': 'lucky boy'
}
response = requests.post(url, params=form_data, headers=headers)
print(json.loads(response.content.decode('UTF-8')))
import requests

proxies = {
    "https": "http://127.0.0.1:8888",
}

url = "https://www.vmgirls.com/"
# 挂在charles的代理上
resp = requests.get(url, proxies=proxies, verify=False, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})

print(resp.text)

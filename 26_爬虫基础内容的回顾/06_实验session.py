import requests

session = requests.session()

session.headers['User-Agent'] = ""
session.cookies['a'] = "b"
session.cookies['a'] = "c"

print(session.cookies)

import re  # 导入re正则模块

# search  只匹配一次
# print(re.search("a", '123456'))
# print(re.search("[a-z]", '123456'))
# print(re.search("[a-z]", '123x456'))
# print(re.search("[a-z][a-z]", '123x456'))
# print(re.search("[a-z][a-z]", '123ab456'))
# print(re.search("[a-z][a-z]", '123ax456b'))
# print(re.search("1[3-9][0-9]{9}", '15611833906'))
# print(re.search("1[3-9][0-9]{9}", '15611833906a'))  # 包含 也就是字符串中包含我要的则为成功
# print(re.search("1[3-9][0-9]{9}", 'x15611833906a'))  # 包含 也就是字符串中包含我要的则为成功
# print(re.search("^1[3-9][0-9]{9}", 'x15611833906a'))
# print(re.search("^1[3-9][0-9]{9}", '15611833906a'))
# print(re.search("^1[3-9][0-9]{9}$", '15611833906a'))  # 完全匹配
# print(re.search("^1[3-9][0-9]{9}$", '15611833906'))  # 完全匹配
# print(re.search("^1[3-9][0-9]{9}$", '1561183390'))  # 完全匹配

# 获取匹配的内容
# print(re.search("^1[3-9][0-9]{9}$", '15611833906').group())  # 完全匹配









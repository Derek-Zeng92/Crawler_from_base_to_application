import re  # 导入re正则模块

# match  只匹配一次  必须从第一位开始 类似于 search("^")
# print(re.match("a", '123456'))
# print(re.match("[a-z]", '123456'))
# print(re.match("[a-z]", '123x456'))
# print(re.search("[a-z]", '123x456'))
# print(re.match("[a-z][a-z]", '123x456'))
# print(re.search("[a-z][a-z]", '123ab456'))
# print(re.search("[a-z][a-z]", '123ax456b'))
# print(re.search("1[3-9][0-9]{9}", '15611833906'))
# print(re.search("1[3-9][0-9]{9}", '15611833906a'))  # 包含 也就是字符串中包含我要的则为成功
# print(re.match("1[3-9][0-9]{9}", 'x15611833906a'))  # 包含 也就是字符串中包含我要的则为成功
# print(re.search("^1[3-9][0-9]{9}", 'x15611833906a'))
# print(re.search("^1[3-9][0-9]{9}", '15611833906a'))

# 获取匹配的内容
# print(re.match("1[3-9][0-9]{9}$", '15611833906').group())  # 完全匹配
# 等同于下方
# print(re.search("^1[3-9][0-9]{9}$", '15611833906').group())  # 完全匹配
print(re.search("^1[3-9][0-9]{9}$", 'a15611833906').group())  # 完全匹配
# AttributeError: 'NoneType' object has no attribute 'group'








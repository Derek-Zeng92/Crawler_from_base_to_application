import re
str = "<b>加粗</b><b>加粗的</b><b>加粗的的</b>"
# 非贪婪
# print(re.search('<b>.*?</b>', str))
# print(re.findall('<b>.*?</b>', str))
# 贪婪
# print(re.search('<b>.*</b>', str))
# print(re.findall('<b>.*</b>', str))

# ()
# val = re.search('<b>(.*?)</b>', str)
val = re.search('<b>.*?</b>', str)
print(val.group())
print(val.groups())  # 如果有多个括号的时候 可以使用groups将值单独取出


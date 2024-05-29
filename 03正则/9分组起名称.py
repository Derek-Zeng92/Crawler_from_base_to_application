import re
myStr = "abcd1"
print(re.search("(?P<number>\d+)", myStr).group(0))
# 当有多个子存储的时候 使用别名比较方便
# print(re.search("(?P<number>\d+)", myStr).group('number'))
print(re.search("(?P<asd>\d+)", myStr).group('asd'))
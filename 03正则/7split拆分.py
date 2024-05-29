import re
myStr = "abc1\rde\t2\ndd3fg"
# 按照数字进行拆分
# print(re.split("\d", myStr))
# print(re.split("\d", myStr, maxsplit=2))
# print(re.findall("\s", myStr))  # 匹配空白符
# print(re.findall("\S", myStr))

# 按照空白符进行拆分
print(re.split('\s', myStr))


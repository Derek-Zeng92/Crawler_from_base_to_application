import re

# re.M 对于^$影响
# \A 和 \Z 和^ $ 一样的   只有在re.M时有区别
myStr = "abcd\nabcd"
# print(re.findall("^a", myStr))
# print(re.findall("\Aa", myStr))

print(re.findall("^a", myStr, re.M))
print(re.findall("\Aa", myStr, re.M))
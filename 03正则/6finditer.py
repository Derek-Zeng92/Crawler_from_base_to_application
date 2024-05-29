import re
obj = re.finditer("[a-z]", "abcdefg")
# obj = re.findall("[a-z]", "abcdefg")
# print(obj)
# print(next(obj))
# print(next(obj))
# print(next(obj))
for i in obj:
    print(i.group())

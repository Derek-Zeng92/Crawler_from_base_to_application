import re
# pattern = re.compile("^1[3-9][0-9]{9}", re.I)
pattern = re.compile("^1[3-9][0-9]{9}")
# print(pattern.search('15611833906a'))
print(pattern.search('15611833906a').group())

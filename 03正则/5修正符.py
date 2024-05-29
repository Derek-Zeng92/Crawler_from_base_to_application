import re
# re.I 是匹配对大小写不敏感
# re.M 多行匹配，影响到^和$
# re.S 使.匹配包括换行符在内的所有字符

myStr = """
<a href="http://www.baidu.com">百度1</a>
<A href="http://www.baidu.com">百度</A>
<a href='http://www.baidu.com'>百度2</a>
<a href='http://www.tengxun.com'>腾
讯</a>
"""
# 匹配所有的正常的a链接  小写
# print(re.findall("<a href=\"http://www.baidu.com\">百度</a>", ""))
# 修正符号
# 匹配大小写
# print(re.findall('(<a href="(.*?)">(.*?)</a>)', myStr, re.I))

# 匹配大小写 多行匹配  可以匹配换行符
print(re.findall('(<a href=[\'"](.*?)[\'"]>(.*?)</a>)', myStr, re.I|re.M|re.S))

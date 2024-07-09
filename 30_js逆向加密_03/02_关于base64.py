import base64

# # 把字节存储成base64的字符串
# s = "基浪费"
# bs = s.encode("utf-8")
# print(bs)
#
# # 把字节编码成base64的字节
# b64bs = base64.b64encode(bs).decode()
# print(len(b64bs))  # =做填充的. 36  160  12  计算出来的长度一定是4的倍数
# print(b64bs)
#
# # b'5Z+65rWq6LS5' => 里面的东西都来自于ascii  GBK,UTF-8兼容ascii


# 通过爬虫得到: 5Z+65rWq6LS5
s = '5Z+65rWq6LS5'
bs = base64.b64decode(s)
print(bs)
print(bs.decode('utf-8'))
# 后面该解密就解密.xxxxx

# 杂乱的字节转化成base64:  base64.b64encode(bytes).decode() =>得到base64字符串
# 得到杂乱的base64字符串,还原成字节: base64.b64decode(s) => 得到字节


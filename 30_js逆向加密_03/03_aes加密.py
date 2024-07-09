# # Cipher 各种加密器
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad
# import base64
#
# # # 1.创建加密器
# # # MODE_ECB  -> 不需要IV
# # # MODE_CBC  -> 需要IV
# # aes = AES.new(key=b'abcdefgjljjhjejx', mode=AES.MODE_CBC, IV=b'0123456789123456')
# #
# # # 2. 加密一段数据试试
# # s = "我发给杨老师了。 请杨老师下课发给我.."
# # bs = s.encode("utf-8")
# # bs = pad(bs, 16)  # 填充，aes大多数是16bit
# # result = aes.encrypt(bs)
# # # print(result)  # 加密后的东西是杂乱五张的字节。。。。
# # # 需要对字节进行b64的处理
# # ss = base64.b64encode(result).decode()
# # print(ss)
#
# # yEd9BHZ7HGvG8/WYw/bCO+uxrUGROJvWQadrkGcmoRiHrXtY88LVv5X6m8OwsNyS65UP+w9HejwVg8o1FlHDjg==
# # 解密
# s = 'yEd9BHZ7HGvG8/WYw/bCO+uxrUGROJvWQadrkGcmoRiHrXtY88LVv5X6m8OwsNyS65UP+w9HejwVg8o1FlHDjg=='
# aes = AES.new(key=b'abcdefgjljjhjejx', mode=AES.MODE_CBC, IV=b'0123456789123456')
#
# result = aes.decrypt(base64.b64decode(s))  # 这里只能解密字节
# r = unpad(result, 16)
# print(r.decode("utf-8"))
#
# # encrypt 加密
# # decrypt 解密


# 9b2c509eaabc228dc17ddaed9e414ef5
# 16进制的数字 => 字节
import binascii

# binascii.a2b_hex把16进制数字转化成字节
print(binascii.a2b_hex("9b2c509eaabc228dc17ddaed9e414ef5").__len__())
# binascii.b2a_hex把字节， 转化成16进制数字

# 区分16进制数字，base64 看组成。，。。。

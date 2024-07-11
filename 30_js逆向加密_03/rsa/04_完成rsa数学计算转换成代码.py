
# s = "10001"  # 十六进制的数字的字符串形式
# i = int(s, 16) # 直接转换成十进制整数
# print(i)
#

e = 0x10001  # 65537  "10001"
n = 0xbe44aec4d73408f6b60e6fe9e3dc55d0e1dc53a1e171e071b547e2e8e0b7da01c56e8c9bcf0521568eb111adccef4e40124b76e33e7ad75607c227af8f8e0b759c30ef283be8ab17a84b19a051df5f94c07e6e7be5f77866376322aac944f45f3ab532bb6efc70c1efa524d821d16cafb580c5a901f0defddea3692a4e68e6cd
# print(e)
# print(n)

ming = "iloveyou"[::-1]  # sorry. 翻转过来....
# 字符串怎么变成 数字
import binascii
m = binascii.b2a_hex(ming.encode())  # 字节转换成十六进制
s = m.decode()
m = int(s, 16)  # 十六进制字符串转换成十进制数字
# print(m)
# 3abca


mi = m ** e % n
# print(mi)

# python十进制转换成16进制
print(hex(mi).replace("0x", ""))
# ?? 解密???

# JSEncrypt -> Crypto
from Crypto.PublicKey import RSA
RSA.import_key()

import binascii
def rsa_encrypt(e, n, en_str):
    en_str = en_str[::-1]
    m = binascii.b2a_hex(en_str.encode())  # 字节转换成十六进制
    s = m.decode()
    m = int(s, 16)
    mi = m ** e % n
    return hex(mi).replace("0x", "")

# 21:29 继续

r = rsa_encrypt(e, n, "123456")
print(r)
# b2927281520eba726728c6f5e9579228a3102f1462c52d708ba8ee622b2124a97545d0e3a6d0315bd84e457e7550ab2357e3c019fe23bf4a57ab2ead172d2e9ce8ae1e167d54a4530a200ba9be5b2fbe08b7cbfe07f914c3c09ccfa37488cc531f9452f625e0195ab41ec88546378ae304f5f774aa2de8891446ff77aae799d8
# b2927281520eba726728c6f5e9579228a3102f1462c52d708ba8ee622b2124a97545d0e3a6d0315bd84e457e7550ab2357e3c019fe23bf4a57ab2ead172d2e9ce8ae1e167d54a4530a200ba9be5b2fbe08b7cbfe07f914c3c09ccfa37488cc531f9452f625e0195ab41ec88546378ae304f5f774aa2de8891446ff77aae799d8


# triple DES  3DES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

des = DES.new(key=b'abcdefgs', mode=DES.MODE_CBC, IV=b'1j2h3bd3')
#
# s = "你好啊".encode("utf-8")
# s = pad(s, 8)
# bs = des.encrypt(s)
# print(bs)


mi = b'*\xf4\x0f\x97%\xd7\xd2\x11"\xfc1\x1f\xbd"\xf4\xef'
s = des.decrypt(mi)
s = unpad(s, 8)
print(s.decode("utf-8"))


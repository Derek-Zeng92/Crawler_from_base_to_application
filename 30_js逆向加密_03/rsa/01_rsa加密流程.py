# from Crypto.PublicKey import RSA  # 这是处理秘钥的
#
# # 想要加密或者解密. 必须先搞定公钥和私钥
#
# # 生成秘钥
# key = RSA.generate(2048)
# # # print(key)  # 此时此刻. 这里有一个私钥
# # private_key = key.exportKey(format='PEM')  #  key.export_key()一样
# # print(private_key.decode())
# #
# # # 如何获取到公钥
# # public_key = key.public_key().export_key()
# # print(public_key.decode())
# # 写出私钥
# with open("private.pem", mode="wb") as f:
#     f.write(key.export_key())
# # 写出公钥
# with open("public.pem", mode="wb") as f:
#     f.write(key.public_key().export_key())
#

# 加密流程(我们最有用的地方) 我们在客户端(js)
# from Crypto.PublicKey import RSA  # 管理秘钥的
# from Crypto.Cipher import PKCS1_v1_5  # 用来加密的
# import base64
#
# # # 1. 加载秘钥(公钥)
# # pub_key = RSA.import_key(open("public.pem", mode='rb').read())
# # # 2. 创建加密器
# # rsa = PKCS1_v1_5.new(key=pub_key)
# # # 3. 加密
# # s = "我爱你".encode("utf-8")
# # bs = rsa.encrypt(s)
# # # print(bs)
# # print(base64.b64encode(bs).decode())
# # # rsa加密后的东西. 如果不是纯数学算法. 每次都是随机的.


# # 解密的流程(我们几乎不用)
# mi = 'bi6ZYvE/CULAfWe//klLpLeBi/Zo6vMNd9eD4LDlu7XvUdpFG90YQ0An+zXa7nt/6Lgmltck71i1eQz0KQnFeorxhK+JqCey7H2MejX/qmmy1Mwb98NQxwO8luVrHE7WibirnEuKGdhFzpBZG8zUAbp0hQeB0gBBCfFvl+rBWsjYRFI83x/XHmRYidq0o7GkN+zfWdeTiuEe7bbB0zxO3k6gwuEVRS79+NNjPnHb9PqfQR6qadZ3cDGazxa2MZ8UVRhMDL7k1rCr09n2ivLhi/EWNlPeGaXXSHO1JVmSC2OFvXPeza0butX15NnotSRGBPuzg5vMQ8SDByOeAKUPxQ=='
#
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_v1_5
# import base64
# # 1. 加载私钥
# private_key = RSA.import_key(open("private.pem", mode="rb").read())
# # 2. 创建加密器
# rsa = PKCS1_v1_5.new(key=private_key)
# # 3. 解密
# result = rsa.decrypt(base64.b64decode(mi), "永不着...")
#
# print(result.decode("utf-8"))

# def func():
#     print("谁呀")
#
# a = 10
# b = 20
# c = a + b
# print(c)
# func()
# func()
# # step over 过步. 标准行, 一行行走
# # step into 进步. 如果该行是函数调用. 进入到函数内部进行逐行调试
# func()
# func()
# func()
# func()
# func()
#
# for i in range(65536):
#     try:
#         print("123")
#         print("456")
#     except Exception as e:
#         print(e)
#         print(i)
#         print("可能会出问题的变量 ")
# # debug -> 调试程序的.
#
# print("呵呵")
#
#

import json

import requests

dic = {
    "imageCaptchaCode":"3jyt",
    "password":"UQ6+uI0M28h6P1SMTNV6PFQ6iAaihOrhfHb0TC273wdGbuYFtPSaTg7iWCCun6RRND4LdVixCbE0P6PGuGOFA3CREYhibzLzfxrQwqA3lQycJydCSSchAbVl339IKSWoXNsxINTvnsQ3mCJPmSivDuVH8PGkXt69BXgGXIovTew=",
    "userName":"18614075987",
}
#
# print(json.dumps(dic))

resp = requests.post("http://www.baidu.com", data=json.dumps(dic).replace(" ", ""))
resp = requests.post("http://www.baidu.com", json=dic)
print(resp.request.body)
# lst = [11,22,33]
# ind = 99
# if ind >= len(lst):
#     pass
# else:
#     print(lst[ind])
# 运行过程中产生的错误。 叫异常

# 连接请求失败（服务器， 反爬， 网络波动， xxxxx）
# try:  # 尝试去执行一些代码
#     print("我去你家了")
#     print("你不在加")
#     print(1/0)  #
#     print(77777)  # ? 会A， 不会B
# except Exception as xxx:  # 7
#     pass
# print("我要上天")

# print(1/0)  # 向外丢出来一个错误信息. 如果没人管
# print("我要上天")  # 看不到

# 连接请求失败（服务器， 反爬， 网络波动， xxxxx）
import time

count = 8
for i in range(count):
    try:
        # 内容 = 发送请求
        # print(1/0)  # 你写错了
        break  # ?
    except Exception as e:
        print("出错了", e)
        time.sleep(10)  # 让程序暂停10秒

# 解析内容

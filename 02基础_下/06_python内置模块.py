# print()
# len()
# range()
# # built-in 不需要导入。直接能用

# # random 随机
# import random
# print(random.randint(10, 11))  # 随机产生一个整数
# lst = [11, 22, 33]
# print(random.choice(lst))  # 随机从列表中获取一个内容

# import time
# print(time.time())  # 从1970-1-1 0 0 0 -> 现在经过了多少秒
# # 你需要注意。 前端， java， 其他语言的时间戳单位是毫秒
# # 伪装成前端的时间戳
# t = int(time.time() * 1000)
# print(t)
# # 1653664705938

import os   # 用来创建文件夹，判断文件夹或者文件, 和文件路径相关
# # os.makedirs("abc/def/hehe")  # 一次性创建很多层文件夹
# p1 = "工程类"
# p2 = "一级建造师"
# p3 = "考点练习"
#
# # 工程类/以及建造师/考点联系
# os.path.join() 路径拼接
# real_path = os.path.join(p1, p2, p3)  # p1 + "/" + p2 + "/" + p3
# os.makedirs(real_path)

# for i in range(10):
#     # 判断路径是否存在
#     if not os.path.exists(f"hehe/chi_{i}"):
#         os.makedirs(f"hehe/chi_{i}")

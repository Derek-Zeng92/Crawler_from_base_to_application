# print(1 < 2)
# 在python中不仅仅可以用True, 或者False来表示真假
# print(bool(10086))  # True
# print(bool(1))  # True
# print(bool(0))  # False
# print(bool(-1))  # True

# print(bool("你好啊"))  # True
# print(bool(" "))  # True
# print(bool(""))  # False

# print(bool([12345]))  # True
# print(bool([]))  # False
#
# # 在python中, 只要是空的东西. 都是False, 只有有东西就是True
#
# print(bool(None))  # False
# print(bool([0]))  # True

a = [123456]  # ??? 从网页上来的任意的数据
if a:  # 大量的用这个东西
    print(a[0])
else:
    print("拜了个拜")
#  7   9

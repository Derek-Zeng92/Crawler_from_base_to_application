
# lst = ["赵本山", "王大陆", "大嘴猴", "马后炮"]
# # # 列表的修改。 直接用索引位置进行重新赋值就可以了
# # lst[1] = "张同学"
# # print(lst)
#
# lst.insert(1, "赵敏")
# print(lst)

# lst = ["赵本山", "王大陆", "大嘴猴", "马后炮"]
# lst1 = ["张无忌", "马皇后"]
#
# # 合并
# lst.extend(lst1)
# print(lst)

# range是用来数数的
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# # for循环。
# for i in range(1, 10):  # range(n) 从0到n-1  range(m, n)  # range(m, n)  m开始, 到n-1
#     print(i)
#
# lst = ["赵本山", "王大陆", "大嘴猴", "马后炮"]
# # 请记住下面的代码, 要清楚item的含义
# for item in lst:  # item就是列表中的每一个
#     print(item)
#
# # 樵夫希望可以拒绝调试丑陋的代码
#
lst = ["alex", "wusir", "sylar", "哈哈", "dsb", "cjdsb"]
# # lst[1] = "Wusir"  # ????77777777777    999
# # # 列表中所有人的名字的首字母改成大写
# # for item in lst:  # 只能拿到元素, 有可能需要索引
# #     # print(item)
# #     s = item.capitalize()  # 把一句话的首字母变成大写
# #     # 索引
# #
# #     print(s)
# # print(lst)  # ['Alex', 'Wusir', 'Sylar', '哈哈']

# 循环的时候可能是需要索引 得具体分析你的需求
for i in range(len(lst)):    # len()可以拿到列表的长度(多少个元素)
    # print(i)
    # print(lst[i])
    s = lst[i].capitalize()
    lst[i] = s  # 修改
print(lst)

# # 记住以下循环的方案
# for item in lst:   循环元素
# for i in range(len(lst)):  循环索引, 元素: lst[i]



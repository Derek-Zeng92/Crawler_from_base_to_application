
dic = {
    "jay": "周杰伦",
    "wlh": "王力宏",
    "glnz": "马尔扎哈",
    # "jay": "周杰伦"
}

# print(dic)
# print(dic["jay"])  # 必须确保key存在, 如果不在. 报错
# print(dic['jay'])
# print(dic.get("jayyyyuyyyyy")) # get能拿到结果, 如果不在,返回None

# if dic.get("jayyyyyyy"):
#     pass
# else:
#     pass

# 绝大多数情况下. 你是知道key是啥的.


# # 字典的新增和修改
# dic['alz'] = "阿里扎"  # key不存在就是新增
# dic['glnz'] = "古力娜扎"  # key存在就是修改
#
# # 综上.dic[key] = value  相当于把数据保存在字典中
# print(dic)

# # 字典循环遍历
# # 1. 直接循环, 就是key
# for k in dic:
#     print(k)
#     print(dic[k])

# # 2.直接拿到key和value, 需要借助item()操作
# for k, v in dic.items():
#     print(k)
#     print(v)


# 接下来是今天最重要的一个东西.
wf = {
    "name": "汪峰",
    "age": 22,
    "wife": {
        "name": "子怡",
        "age": 23,
        "hobby": ["演戏", "上综艺", "唱歌"],
        "粉丝": [
            {"name": "樵夫", "age": 19, "hobby": [11,222,33]},
            {"name": "alex", "age": 22, "hobby": [11,222,33]},
            {"name": "胡辣汤", "age": 38, "hobby": [11,222,33]}
        ]
    },
    "hobby": ["皮裤", "瑜伽裤", "短裤", "裤裤"],
    "children": [
        {"name": "孩子1", "age": 5},
        {"name": "孩子2", "age": 6},
        {"name": "孩子3", "age": 7},
    ]
}
# # 请打印汪峰老婆的名字
# print(wf['wife']['name'])
# # 我想看看汪峰老婆的第二个爱好
# print(wf['wife']['hobby'][1])
# # 拿到汪峰第二个孩子的年龄
# print(wf['children'][1]['age'])

# 我想看到汪峰每个孩子的名字
# for item in wf['children']:
#     # print(item)  # ? {'name': '孩子3', 'age': 7}  # 77   99
#     print(item['name'])
# 我想看到汪峰老婆的每一个爱好

# for item in wf['wife']['hobby']:
#     print(item)
#
# for item in wf['wife']['粉丝']:  # [{}, {}, {}]
#     print(item['age'])  # 自己顺.
#
# # 核心解决方案, 一层一层的往出剥洋葱



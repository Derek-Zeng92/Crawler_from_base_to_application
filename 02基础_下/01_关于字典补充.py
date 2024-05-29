dic = {
    "name": "王峰",
    "age": 18,
    "wife": {
        "name": "章子怡",
        "age": 19,
    }
}

v = dic.get("马化腾")  # 7
# 如果key存在. 则根据key把value拿出来. 返回
# 如果key不存在. 则直接返回第二个参数

if not v:
    v = "qq老大"
print(v)


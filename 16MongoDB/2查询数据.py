from pymongo import MongoClient
import re
# 连接mongodb
conn = MongoClient('localhost')
# 选择数据库
db = conn.test

# 查询所有
# data = db.user.find()
# print(next(data))
# for i in data:
#     print(i)


# 查询一条
# data = db.user.find_one()
# print(data)

# 添加条件查询
# data = db.user.find({"name": "lucky"})
# 模糊查询
# data = db.user.find({"name": re.compile('l')})
# data = db.user.find({"name": re.compile('z')})

# 排序
# data = db.user.find({}).sort('age', 1)
# data = db.user.find({}).sort('age', -1)
data = db.user.find({}).sort('age', -1).limit(2)
# print(next(data))
for i in data:
    print(i)
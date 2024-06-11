from pymongo import MongoClient
# 连接mongodb
conn = MongoClient('localhost')
# 选择数据库
db = conn.test

# 插入一条数据
# data = db.user.insert_one({"name": "lucky", 'age': 18, 'sex': 'man'})
# print(data.inserted_id)
# 插入多条数据
data = db.user.insert_many([{"name": "zhangsan", 'age': 20, 'sex': 'women'},{"name": "lucky", 'age': 18, 'sex': 'man'}])
print(data.inserted_ids)

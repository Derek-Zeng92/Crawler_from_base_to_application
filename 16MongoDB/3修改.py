from pymongo import MongoClient
import re
# 连接mongodb
conn = MongoClient('localhost')
# 选择数据库
db = conn.test

# 修改一条
# data = db.user.update_one({'name': 'lucky'},{'$set':{'age': 20}})
# print(data.modified_count)

# 修改多条
data = db.user.update_many({'name': 'lucky'},{'$set':{'age': 18}})
print(data.modified_count)
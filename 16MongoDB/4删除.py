from pymongo import MongoClient
import re
# 连接mongodb
conn = MongoClient('localhost')
# 选择数据库
db = conn.test

# 删除一条
# data = db.user.delete_one({'name': 'zhangsan'})
# print(data.deleted_count)  # 删除的条数

# 删除多条
data = db.user.delete_many({'name': 'lucky'})
print(data.deleted_count)  # 删除的条数
import redis
# r = redis.StrictRedis(host='127.0.0.1', port=6379, password='123456', decode_responses=True)
r = redis.StrictRedis(password='123456', decode_responses=True)
# print(r)

# 设置
# print(r.set("name", "lucky dad"))
# print(r.get('name'))

# 批量设置
# print(r.mset({'name':'lucky', 'age': 18}))
# print(r.mget('name', 'age'))

# print(r.type('name'))

print(r.getset("name", "李四"))
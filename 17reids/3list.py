import redis
# r = redis.StrictRedis(host='127.0.0.1', port=6379, password='123456', decode_responses=True)
r = redis.StrictRedis(password='123456', decode_responses=True)

# 设置
# print(r.lpush('list', 1, 2, 3))
# print(r.rpush('list', 4, 5, 6))

# 获取
# print(r.lrange('list', 0, -1))

# 元素个数
# print(r.llen('list'))

print(r.type('list'))
import redis
# r = redis.StrictRedis(host='127.0.0.1', port=6379, password='123456', decode_responses=True)
r = redis.StrictRedis(password='123456', decode_responses=True)

# 添加值
# print(r.sadd('set1', 'a', 'b', 'c'))
# print(r.sadd('set2', 'a', 'b', 'd'))

# 获取值
# print(r.smembers('set1'))

# 元素个数
# print(r.scard('set1'))

# print(r.sdiff('set1', 'set2'))
# print(r.sinter('set1', 'set2'))

print(r.type('set1'))
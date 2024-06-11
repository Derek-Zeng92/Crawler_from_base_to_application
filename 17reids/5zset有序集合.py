import redis
# r = redis.StrictRedis(host='127.0.0.1', port=6379, password='123456', decode_responses=True)
r = redis.StrictRedis(password='123456', decode_responses=True)

# 添加值
# print(r.zadd('zadd', {"a": 1, 'b': 2, 'c': 3}))
# print(r.zcard('zadd'))
# 返回权重
print(r.zscore('zadd', 'a'))

print(r.type('zadd'))

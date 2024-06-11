import redis
# r = redis.StrictRedis(host='127.0.0.1', port=6379, password='123456', decode_responses=True)
r = redis.StrictRedis(password='123456', decode_responses=True)

# 设置
# print(r.hset("hash", "name", "lucky"))
# print(r.hget("hash", "name"))

# 获取所有
# print(r.hgetall('hash'))

# 批量设置
# print(r.hmset("myhash",{"name":"lucky", "age": 18}))

# 获取所有的hash的field
# print(r.hkeys("myhash"))

# 获取hash所有的值
# print(r.hvals('myhash'))

print(r.type('myhash'))
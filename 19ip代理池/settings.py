'''
当前项目的全局配置文件
'''
# redis的配置
HOST = '127.0.0.1'
PORT = 6379
PASSWORD = '123456'
DB = 0
SCORE = 100  # 默认最高权重100
MIN_SCORE = 95  # 最低权重
ZSET_NAME = 'proxy_redis'   # 有序集合名词
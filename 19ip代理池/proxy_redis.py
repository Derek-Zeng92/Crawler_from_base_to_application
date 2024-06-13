'''
对于ip的处理
存储、ip可用不可用进行处理
'''
import random

from settings import *  # 导入所有的配置
import redis
class ProxyRedis:
    def __init__(self):
        # 连接reids数据库
        self.r = redis.Redis(host=HOST, port=PORT, password=PASSWORD, db=DB, decode_responses=True)

    # 添加ip
    def zset_zadd(self, ip):
        self.r.zadd(ZSET_NAME, {ip: SCORE})

    # 降低权重
    def zset_zincrby(self, ip):
        # 先查出权重
        score = self.r.zscore(ZSET_NAME, ip)
        # 判断当前的权重是否小于最低权重
        if score > MIN_SCORE:
            # 将当前权重减少1
            self.r.zincrby(ZSET_NAME, -1, ip)
        else:
            # 删除ip
            print('ip:', ip,f'低于最低权重${MIN_SCORE}，删除')
            self.r.zrem(ZSET_NAME, ip)

    def get_ip(self):
        '''
        返回高权重的ip
        '''
        ip = self.r.zrangebyscore(ZSET_NAME, SCORE, SCORE, 0, -1)
        if ip:
            # 随机返回一个ip
            return random.choice(ip)
        else:
            ip = self.r.zrangebyscore(ZSET_NAME, 80, SCORE, 0, -1)
            if ip:
                # 随机返回一个ip
                return random.choice(ip)
            else:
                print('实在没有了~')

    # 返回所有的ip  以供test_ip 进行测试
    def zset_zrange(self):
        return self.r.zrange(ZSET_NAME, 0, -1)



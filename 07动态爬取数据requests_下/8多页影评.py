'''
# 多页url
https://movie.douban.com/review/best/?start=0
https://movie.douban.com/review/best/?start=20
https://movie.douban.com/review/best/?start=40
https://movie.douban.com/review/best/?start=60
'''
# 怎样循环获取多页url
# 抓取3页数据
for i in range(0, 81, 20):
    # 要求 输出当前第几页
    print('当前为第...页')
    print(f'https://movie.douban.com/review/best/?start={i}')

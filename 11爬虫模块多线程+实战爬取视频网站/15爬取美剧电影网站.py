# 美剧网址
url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-1.html'
# 抓取思路
# 1 先看当前网站是什么类型的视频网站
# 2 查看当前网站的视频 是怎样加载的(1一次性加载的 还是分了多个视频段进行加载的)
# 3 如果是多个片段的文件  需要找到当前包含多个片段文件的地址

# 数据量很少的m3u8文件
# 通过页面源代码找到了当前的url
#  "url": "https://new.qqaku.com/20211117/iHVkqQMI/index.m3u8",


# https://new.qqaku.com/20211117/iHVkqQMI/index.m3u8
'''
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2523000,RESOLUTION=1920x1080
/20211117/iHVkqQMI/2523kb/hls/index.m3u8
                  2523kb/hls/index.m3u8
'''
# 返回一堆ts  url的文件
# https://new.qqaku.com/20211117/iHVkqQMI/2523kb/hls/index.m3u8
# https://new.qqaku.com/20211117/iHVkqQMI/2523kb/hls/index.m3u8

# https://new.qqaku.com/20211117/iHVkqQMI/20211117/iHVkqQMI/2523kb/hls/index.m3u8

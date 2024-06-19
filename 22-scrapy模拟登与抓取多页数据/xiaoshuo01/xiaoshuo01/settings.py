# Scrapy settings for xiaoshuo01 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiaoshuo01'

SPIDER_MODULES = ['xiaoshuo01.spiders']
NEWSPIDER_MODULE = 'xiaoshuo01.spiders'
LOG_LEVEL = 'ERROR'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xiaoshuo01 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False   # 当前打开注释  使用settings里面的cookie  这种就是写死了

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Cookie': 'acw_tc=2760828b17187669188055278ea086cf2ee52e47cbd3c9c1197d0b04b307a1; GUID=50277ed9-4fe7-410c-a85a-6d9ebc074670; acw_sc__v2=66724d473954ad398f73d19d8c41faca0745a463; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1718766920; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F98%252F90%252F96139098.jpg-88x88%253Fv%253D1650527904000%26id%3D96139098%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BqYx51ZhI1%26e%3D1734319109%26s%3D451a057538a89d4b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296139098%22%2C%22%24device_id%22%3A%221902e7ddf9d8c2-036727f15d1699-26001c51-2073600-1902e7ddf9e947%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2250277ed9-4fe7-410c-a85a-6d9ebc074670%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1718767471; tfstk=fWVBrfVmqHxQ-lasqvQZGzpkSnh57k1qVUg8ozdeyXhp23Uxb2KLYzn7VlogVYbn40n74zeF7s54-ycowusVgs-cY4EaA2H-wa3tP4JZ2TUb-yckSfOa7QzHFzNGUWh82fHtz4h-JBhR5f3mubdKeBp9Xc0-w0E-vVCtyqLKJYnpWbnvl46Ixy_6bkhXQeyuJcObS53Klp4IfQd81okID_i6wQFsRP2qlkRfUmemYxo0X1RINP37fxyCcBZ7yr2-C7td8oU8x5GnGT7nhRea3vw1vQiaT4MxwATJwPG8pYFSMsKsSRUUeWqBPQ33TSkSmA_JZYlTgxeYAUb0WX38qxVPmBmLyrV03j1Bm2wTlfsrYIobajvW5xAS5m715LvrOItwjodwcYMKS2MN5NtLEv3i5m715LvopV0IbN_6v8f..; ssxmod_itna=eqRhqIxh8i4xzxAOD5GkKDCUDkUb81DRGx=8x0y04eGzDAxn40iDtxo54Dug/B+1CbPQbhrMFoQg2m5Km3ONWDU4i8DCqx3=iDem=D5xGoDPxDeDADYojDAqiOD7qDdvk5Hz8DbxYpMDYvaDQ5sVxDF01F7D4i7DD5QFx07qf9tDGytkUqxzoxxVxDrFxYCTSK4+t0DvxG1q40HdeMtvZAjnUw1+f3LZpb7DlI0DCIC399mDB+8B=HsvYr3wYxeTcc4LG0KeY2tYnhcqYr58YeosDx4MQi5xEhKe72cnXqDicuW4D===; ssxmod_itna2=eqRhqIxh8i4xzxAOD5GkKDCUDkUb81DRGx=4nK3DQDlh4QId08D+gtjYoD=='
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xiaoshuo01.middlewares.Xiaoshuo01SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xiaoshuo01.middlewares.Xiaoshuo01DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'xiaoshuo01.pipelines.Xiaoshuo01Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

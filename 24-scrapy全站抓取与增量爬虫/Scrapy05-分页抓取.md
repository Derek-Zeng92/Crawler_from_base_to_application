# scrapy的crawlspider爬虫

##### 学习目标：

1. 了解 crawlspider的作用
2. 应用 crawlspider爬虫创建的方法
3. 应用 crawlspider中rules的使用 

------

### 1、crawlspider是什么

> 回顾之前的代码中，我们有很大一部分时间在寻找下一页的url地址或者是内容的url地址上面，这个过程能更简单一些么？

##### 思路：

1. 从response中提取所有的满足规则的url地址
2. 自动的构造自己requests请求，发送给引擎

对应的**crawlspider就可以实现上述需求，能够匹配满足条件的url地址，组装成Reuqest对象后自动发送给引擎，同时能够指定callback函数**

**即：crawlspider爬虫可以按照规则自动获取连接**

### 2、crawlspider豆瓣TOP250爬虫

> 通过crawlspider爬取豆瓣TOP250详情页的信息
>
> url：https://movie.douban.com/top250

##### 思路分析：

1. 定义一个规则，来进行列表页翻页，follow需要设置为True
2. 定义一个规则，实现从列表页进入详情页，并且指定回调函数
3. 在详情页提取数据

##### 注意：连接提取器LinkExtractor中的allow对应的正则表达式匹配的是href属性的值

### 3、创建crawlspider爬虫并观察爬虫内的默认内容

##### 3.1 创建crawlspider爬虫：

scrapy startproject project

cd project

scrapy genspider -t crawl douban book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p=1

url: 豆瓣图书 https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p=1

##### 3.2 spider中默认生成的内容如下：

```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'douban'
    # allowed_domains = ['https://movie.douban.com/top250']

    start_urls = ['https://movie.douban.com/top250']
    # 匹配页码地址
    link = LinkExtractor(allow=r'start=\d+&filter=')
    # 匹配详情页地址
    link_detail = LinkExtractor(allow=r'https://movie.douban.com/subject/\d+/')
    # allow值什么都不写 则为提取所有的url
    link_all = LinkExtractor(allow=r'')
    rules = (
        # Rule(link, callback='parse_item', follow=True),
        # Rule(link_detail, callback='parse_detail_item', follow=False),
        Rule(link_all, callback='parse_all_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        print(response)
        return item

    def parse_detail_item(self, response):
        item = {}
        print(response)
        return item

    def parse_all_item(self, response):
        item = {}
        print(response)
        return item
```

##### 3.3 观察跟普通的scrapy.spider的区别

在crawlspider爬虫中，没有parse函数

##### 重点在rules中：

1. rules是一个元组或者是列表，包含的是Rule对象
2. Rule表示规则，其中包含LinkExtractor,callback和follow等参数
3. LinkExtractor:连接提取器，可以通过正则或者是xpath来进行url地址的匹配
4. callback :表示经过连接提取器提取出来的url地址响应的回调函数，可以没有，没有表示响应不会进行回调函数的处理
5. follow：连接提取器提取的url地址对应的响应是否还会继续被rules中的规则进行提取，True表示会，Flase表示不会

### 4、crawlspider使用的注意点：

1. 除了用命令`scrapy genspider -t crawl <爬虫名> <allowed_domail>`创建一个crawlspider的模板，页可以手动创建
2. crawlspider中不能再有以parse为名的数据提取方法，该方法被crawlspider用来实现基础url提取等功能
3. Rule对象中LinkExtractor为固定参数，其他callback、follow为可选参数
4. 不指定callback且follow为True的情况下，满足rules中规则的url还会被继续提取和请求
5. 如果一个被提取的url满足多个Rule，那么会从rules中选择一个满足匹配条件的Rule执行

### 5、了解crawlspider其他知识点

- 链接提取器LinkExtractor的更多常见参数

  - allow: 满足括号中的're'表达式的url会被提取，如果为空，则全部匹配

  - deny: 满足括号中的're'表达式的url不会被提取，优先级高于allow

  - allow_domains: 会被提取的链接的domains(url范围)，如：`['https://movie.douban.com/top250']`

  - deny_domains: 不会被提取的链接的domains(url范围)

  - **restrict_xpaths: 使用xpath规则进行匹配，和allow共同过滤url，即xpath满足的范围内的url地址会被提取**

    如：`restrict_xpaths='//div[@class="pagenav"]'`

  - restrict_css: 接收一堆css选择器, 可以提取符合要求的css选择器的链接

  - attrs: 接收一堆属性名, 从某个属性中提取链接, 默认href

  - tags: 接收一堆标签名, 从某个标签中提取链接, 默认a, area

  值得注意的, **在提取到的url中, 是有重复的内容的. 但是我们不用管. scrapy会自动帮我们过滤掉重复的url请求**

- 模拟使用

　　正则用法：　links1 = LinkExtractor(allow=r'list_23_\d+\.html')

　　xpath用法： links2 = LinkExtractor(restrict_xpaths=r'//div[@class="x"]')

　	css用法：  links3 = LinkExtractor(restrict_css='.x')

5.提取连接

- Rule常见参数

  - LinkExtractor: 链接提取器，可以通过正则或者是xpath来进行url地址的匹配
  - callback: 表示经过连接提取器提取出来的url地址响应的回调函数，可以没有，没有表示响应不会进行回调函数的处理
  - follow: 连接提取器提取的url地址对应的响应是否还会继续被rules中的规则进行提取，默认True表示会，Flase表示不会
  - process_links: 当链接提取器LinkExtractor获取到链接列表的时候调用该参数指定的方法，这个自定义方法可以用来过滤url，且这个方法执行后才会执行callback指定的方法

### 总结

1. crawlspider的作用：crawlspider可以按照规则自动获取连接
2. crawlspider爬虫的创建：scrapy genspider -t crawl xxx  www.xxx.com
3. crawlspider中rules的使用：
   + rules是一个元组或者是列表，包含的是Rule对象
   + Rule表示规则，其中包含LinkExtractor,callback和follow等参数
   + LinkExtractor:连接提取器，可以通过正则或者是xpath来进行url地址的匹配
   + callback :表示经过连接提取器提取出来的url地址响应的回调函数，可以没有，没有表示响应不会进行回调函数的处理
   + follow：连接提取器提取的url地址对应的响应是否还会继续被rules中的规则进行提取，True表示会，Flase表示不会

#### 
# # w: 只能写,它会重新创建一个新文件
# # r: 只能读,从文件中读取内容. 如果文件不存在. 则报错
# # windows默认是gbk编码
# f = open("葫芦娃.txt", mode='w', encoding="utf-8")
# # 7777 9999
# f.write("胡辣汤")
# f.write("疙瘩汤")

# f = open("葫芦娃.txt", mode="r", encoding="utf-8")
# # s = f.read()  # 一次性读取所有内容
# # print(s)
#
# for line in f:  # line就是每一行数据
#     line = line.strip()  # 如果还有写错的. 5分钟
#     # 发请求到line
#     print(line)

s = "我是小金刚.我是从网页上抓取到的"
f = open("小金刚.txt", mode="w", encoding="utf-8")
f.write(s)
f.close()


# 如果你下载的是一张图片, mp3, avi, mp4, exe, zip????
# 上述内容, 你从网页上拿到的只能是字节(二进制流) bytes b''
f = open("胡一菲.jpg", mode="wb")  # wb 写入字节模式,bytes, rb 读取字节
f.write(b'从网页上拿到的真实的图片的内容')

# 带b的都是处理的字节


# f = open("xxxx.txt", mode="w", encoding="")
# f.write("123456")
# f.close()  # 忘
#
# f = open("xxxx.txt", mode="w", encoding="")
# f.write("456789")
# f.close()

# with open("xxx", xxxx) as f:
#     pass
#     # 打开这个文件, 你要干嘛

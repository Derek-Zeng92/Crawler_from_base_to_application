from hashlib import md5

# python计算的md5是标准的md5算法. -> 可以直接用python来完成
# 有可能会遇到魔改的md5  -> 需要去抠代码

def func():
    # 1. 创建一个md5的加密对象
    obj = md5()
    # 防止撞库. 加盐.
    obj = md5(b'ljfadslkjflkadsjfkladsjflkadsjfkladsjfkladsjfkladsjfklaewjufiolkewmjioczjdxsiolfhuyaoesinjfoiadshfcklj;aDSZHfkjldashfijuoaeswnhfojikeawhfuiojeawnhjfiueawohfiuoaewshfyouieawhfikuewahfuio9ew')
    # 2. 给这个加密对象增加内容
    obj.update("123456".encode("utf-8"))  # 添加内容 这个内容必须是字节
    # 如果md5实例化是在函数外面那么最终计算的时候. 是多次update的拼接,
    # 3. 看结果.导出32位 十六进制
    result = obj.hexdigest()
    print(result)

func()

from hashlib import sha1, sha256, sha512

obj = sha512()
obj.update("起风了".encode("utf-8"))
print(obj.hexdigest())
